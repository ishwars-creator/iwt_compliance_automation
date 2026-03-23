import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.compliance_page import CompliancePage
from pages.operator_analytics_citation_sum_page import OperatorAnalyticsPage
from utils.config import USERNAME, PASSWORD
import pytest

@pytest.fixture
def operator_analytics_citation_summary(page):
    # ---------- Login & navigate to operator analytics ----------
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    op = OperatorAnalyticsPage(page)
    op.goto_compliace_menu()
    CompliancePage(page).goto_operator_analytics()
    op.select_company()
    op.select_all_mines()
    op.select_all_events()
    
    # ------------------ Get citation count displayed on card -------------
    citation_value = page.locator(
        "//p[normalize-space()='Citations']/following-sibling::p"
    ).inner_text()

    citation_count = int(citation_value.strip())

    print("Citation Count:", citation_count)
    

    # ---------- Hover specific pie slice (Non-S&S) ----------
    pie_slice = page.locator(
        "g.pielayer g.slice path.surface[style*='rgb(255, 99, 71)']"
    ).first

    expect(pie_slice).to_be_visible()

    box = pie_slice.bounding_box()
    assert box, "Pie slice bounding box not found"

    # Move mouse to center of slice
    page.mouse.move(
        box["x"] + box["width"] / 2,
        box["y"] + box["height"] / 2
    )

    # Slight move to force tooltip render
    page.mouse.move(
        box["x"] + box["width"] / 2 + 2,
        box["y"] + box["height"] / 2 + 2
    )

    # ---------- Wait for Plotly tooltip ----------
    page.wait_for_selector("g.hoverlayer g.hovertext text", timeout=5000)

    tooltip_texts = page.locator(
        "g.hoverlayer g.hovertext text"
    ).all_text_contents()

    print("Tooltip texts:", tooltip_texts)

    # ---------- Extract values ----------
    non_ss_percentage = None
    non_ss_citations = None

    for text in tooltip_texts:
        # Extract percentage after "Non-S&S"
        pct_match = re.search(r"S\s*&\s*S:\s*(\d+(\.\d+)?)%", text)
        if pct_match:
            non_ss_percentage = pct_match.group(1) + "%"

        # Extract citations after "Citations :"
        cit_match = re.search(r"Citations\s*:\s*(\d+)", text)
        if cit_match:
            non_ss_citations = cit_match.group(1)    
    
    
     # ---------- Hover specific pie slice (S&S) ----------

    pie_slice = page.locator(
        "g.pielayer g.slice path.surface[style*='rgb(255, 194, 93)']"
    ).first

    expect(pie_slice).to_be_visible()

    box = pie_slice.bounding_box()
    assert box, "S&S pie slice bounding box not found"

    # Move mouse to center of slice
    page.mouse.move(
        box["x"] + box["width"] / 2,
        box["y"] + box["height"] / 2
    )

    # Slight movement to force tooltip render
    page.mouse.move(
        box["x"] + box["width"] / 2 + 2,
        box["y"] + box["height"] / 2 + 2
    )

    # ---------- Wait for Plotly tooltip ----------
    page.wait_for_selector("g.hoverlayer g.hovertext text", timeout=5000)

    tooltip_texts = page.locator(
        "g.hoverlayer g.hovertext text"
    ).all_text_contents()

    print("Tooltip texts:", tooltip_texts)

    # ---------- Extract values ----------
    ss_percentage = None
    ss_citations = None

    for text in tooltip_texts:
        # Extract S&S percentage
        pct_match = re.search(r"S\s*&\s*S:\s*(\d+(\.\d+)?)%", text)
        if pct_match:
            ss_percentage = pct_match.group(1) + "%"

        # Extract citations
        cit_match = re.search(r"Citations\s*:\s*(\d+)", text)
        if cit_match:
            ss_citations = cit_match.group(1)


    
    return {
        "ss_percentage": ss_percentage,
        "ss_citations": ss_citations,
        "non_ss_percentage": non_ss_percentage,
        "non_ss_citations": non_ss_citations,
        "citation_count": citation_count
    }
    

# Validate citations sum on S&S chart distribution to total citations on card

def test_SS_distribution_citation_sum(operator_analytics_citation_summary):
    total_citations = (
        int(operator_analytics_citation_summary["ss_citations"])
        + int(operator_analytics_citation_summary["non_ss_citations"])
    )
    print("S&S Citations:", operator_analytics_citation_summary["ss_citations"])
    print("Non-S&S Citations:", operator_analytics_citation_summary["non_ss_citations"])
    print("Total Citations:", total_citations)
    print("Expected Citations:", operator_analytics_citation_summary["citation_count"])
    assert total_citations == operator_analytics_citation_summary["citation_count"]
    
    

# S&S distribution pie chart: Validate summation of percentage of s&s and non s&s citations, it should be 100%

def test_SS_distribution_percentage_sum(operator_analytics_citation_summary):
    total = (
        float(operator_analytics_citation_summary["ss_percentage"].rstrip("%"))
        + float(operator_analytics_citation_summary["non_ss_percentage"].rstrip("%"))
    )
    print("S&S Percentage:", operator_analytics_citation_summary["ss_percentage"])
    print("Non-S&S Percentage:", operator_analytics_citation_summary["non_ss_percentage"])
    print("Total Percentage:", total)
    assert round(total, 2) == 100.0
    
