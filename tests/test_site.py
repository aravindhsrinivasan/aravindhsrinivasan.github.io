from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.elements = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class PortfolioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.page = Page(cls.html)

    def test_navigation_tabs_and_assets_resolve(self):
        ids = [attrs["id"] for _, attrs in self.page.elements if "id" in attrs]
        self.assertEqual(len(ids), len(set(ids)), "Duplicate element IDs")
        for tag, attrs in self.page.elements:
            for name in ("aria-controls", "aria-labelledby"):
                for target in attrs.get(name, "").split():
                    self.assertIn(target, ids)
            href = attrs.get("href", "")
            if href.startswith("#"):
                self.assertIn(href[1:], ids)
            if tag == "img":
                self.assertTrue((ROOT / attrs["src"]).is_file())
                self.assertTrue(attrs.get("alt"))

    def test_guided_pitch_keeps_recording_out_and_discloses_local_voice(self):
        sections = [
            attrs for tag, attrs in self.page.elements
            if tag == "section" and "slide" in attrs.get("class", "").split()
        ]
        self.assertTrue(sections)
        self.assertTrue(all(attrs.get("data-caption", "").strip() for attrs in sections))
        self.assertFalse(any(tag in ("audio", "source") for tag, _ in self.page.elements))
        self.assertNotIn("base64,", self.html)
        self.assertNotIn("AudioContext", self.html)
        self.assertFalse(list(ROOT.rglob("*.mp3")))
        self.assertIn("item.localService", self.html)
        self.assertIn("No on-device English voice", self.html)
        self.assertIn("not the original recorded voiceover", self.html)

    def test_planned_projects_do_not_link_to_nonexistent_repositories(self):
        project_cards = [
            attrs for tag, attrs in self.page.elements
            if tag == "article" and "project" in attrs.get("class", "").split()
        ]
        self.assertEqual(len(project_cards), 3)
        self.assertEqual(self.html.count("Planned &middot; not yet built"), 2)
        self.assertIn("Local baseline built &middot; not yet published", self.html)
        self.assertIn("60 AI-drafted questions", self.html)
        self.assertIn("all labels remain unreviewed", self.html)
        repo_links = [
            attrs["href"] for _, attrs in self.page.elements
            if attrs.get("href", "").startswith("https://github.com/aravindhsrinivasan/")
        ]
        self.assertEqual(repo_links, [])

    def test_uncleared_metrics_and_targets_stay_out_of_public_payload(self):
        for value in ("93 TB", "8.5K", "8,500", "470 applications", "47%", "73%",
                      "40h", "15 minutes", "15-minute", "Pinnacle", "12,000", "10,000"):
            self.assertNotIn(value, self.html)
        self.assertFalse(any(
            tag == "script" and attrs.get("src", "").startswith(("http:", "https:"))
            for tag, attrs in self.page.elements
        ))


if __name__ == "__main__":
    unittest.main()
