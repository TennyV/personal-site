#!/usr/bin/env python3
"""Generate the branded 1-page NIS2 compliance checklist PDF."""
from fpdf import FPDF

NAVY = (43, 62, 80)
BLUE = (52, 111, 166)
GREY = (102, 102, 102)
LIGHT = (238, 243, 248)
BORDER = (201, 212, 222)
DARK = (34, 34, 34)

sections = [
    ("A. Governance & Registration", [
        "Entity classification (essential vs. important) determined and documented, with the reasoning and data behind it",
        "Registered with the national authority (Poland: KSC Act - deadline October 3, 2026)",
        "Management board has formally approved the cybersecurity risk-management framework and oversees it (personal liability applies)",
        "Management has completed cybersecurity training; a staff awareness program is running",
        "Cybersecurity roles, responsibilities, and authority contact points are assigned and documented",
    ]),
    ("B. Risk-Management Measures (Art. 21)", [
        "Risk analysis performed; information-system security policies adopted",
        "Incident-handling procedure covers detection, analysis, containment, response, and recovery",
        "Backup management in place; disaster recovery tested, not just documented",
        "Business continuity and crisis-management plan in place",
        "Supply-chain security: direct suppliers and service providers assessed for security posture",
        "Security requirements embedded in acquisition, development, and maintenance of systems",
        "Vulnerability handling and coordinated disclosure process in place",
        "Policies and procedures to assess the effectiveness of the measures themselves",
        "Basic cyber hygiene: patching, hardening, least privilege, network segmentation",
        "Cryptography policy: encryption at rest and in transit where appropriate",
        "Human-resources security, access control, and asset-management policies",
        "Multi-factor or continuous authentication deployed for critical access",
        "Secured voice, video, and text communications; emergency communication channels defined",
    ]),
    ("C. Incident Reporting (Art. 23)", [
        "24-hour early-warning workflow to the CSIRT / competent authority",
        "72-hour full incident notification with initial severity and impact assessment",
        "Final report process delivering within one month of the incident notification",
    ]),
    ("D. Ongoing Compliance", [
        "Audit readiness: evidence register maintained and current (Poland: risk measures due April 2027; first mandatory audits April 2028)",
        "Periodic validation: penetration tests, tabletop exercises, and control reviews on a schedule",
    ]),
]

pdf = FPDF(format="A4", unit="mm")
pdf.set_auto_page_break(False)
pdf.set_margins(11, 10, 11)
pdf.add_page()

page_w = 210 - 22  # printable width

# --- Header ---
pdf.set_font("Helvetica", "B", 17)
pdf.set_text_color(*NAVY)
pdf.cell(0, 8, "NIS2 COMPLIANCE CHECKLIST", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "I", 8)
pdf.set_text_color(*GREY)
pdf.cell(0, 4.5, "23 essential controls  ·  applies to essential and important entities  ·  based on NIS2 Articles 20, 21 & 23 and Poland's KSC Act",
         new_x="LMARGIN", new_y="NEXT")
pdf.ln(1.5)

# --- Table geometry ---
w_num, w_e, w_i, w_done = 8, 16, 16, 20
w_ctrl = page_w - w_num - w_e - w_i - w_done
row_font = 7.6
line_h = 3.4


def header_row():
    pdf.set_fill_color(*NAVY)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 8)
    h = 6
    pdf.cell(w_num, h, "#", border=0, align="C", fill=True)
    pdf.cell(w_ctrl, h, "  Control", border=0, align="L", fill=True)
    pdf.cell(w_e, h, "Essential", border=0, align="C", fill=True)
    pdf.cell(w_i, h, "Important", border=0, align="C", fill=True)
    pdf.cell(w_done, h, "In place?", border=0, align="C", fill=True)
    pdf.ln(h)


def section_row(title):
    pdf.set_fill_color(*LIGHT)
    pdf.set_text_color(*BLUE)
    pdf.set_font("Helvetica", "B", 8.2)
    h = 5
    pdf.cell(page_w, h, "  " + title, border=0, align="L", fill=True)
    pdf.ln(h)


def control_row(n, text):
    pdf.set_font("Helvetica", "", row_font)
    lines = pdf.multi_cell(w_ctrl - 2, line_h, text, dry_run=True, output="LINES")
    h = max(len(lines) * line_h + 1.6, 5)
    x0, y0 = pdf.get_x(), pdf.get_y()

    pdf.set_draw_color(*BORDER)
    pdf.set_line_width(0.15)
    for w in (w_num, w_ctrl, w_e, w_i, w_done):
        pdf.rect(pdf.get_x(), y0, w, h)
        pdf.set_x(pdf.get_x() + w)

    pdf.set_xy(x0, y0)
    pdf.set_text_color(*GREY)
    pdf.cell(w_num, h, str(n), align="C")
    pdf.set_text_color(*DARK)
    pdf.set_xy(x0 + w_num + 1, y0 + 0.8)
    pdf.multi_cell(w_ctrl - 2, line_h, text, align="L")
    pdf.set_xy(x0 + w_num + w_ctrl, y0)
    pdf.set_text_color(*BLUE)
    pdf.set_font("Helvetica", "B", row_font)
    pdf.cell(w_e, h, "YES", align="C")
    pdf.cell(w_i, h, "YES", align="C")

    # drawn checkbox in the "In place?" column
    box = 2.8
    cx = x0 + w_num + w_ctrl + w_e + w_i + w_done / 2 - box / 2
    cy = y0 + h / 2 - box / 2
    pdf.set_draw_color(*GREY)
    pdf.set_line_width(0.25)
    pdf.rect(cx, cy, box, box)

    pdf.set_xy(x0, y0 + h)


header_row()
n = 0
for title, controls in sections:
    section_row(title)
    for text in controls:
        n += 1
        control_row(n, text)

# --- Footer ---
pdf.ln(1.5)
pdf.set_font("Helvetica", "", 7.2)
pdf.set_text_color(*GREY)
pdf.multi_cell(page_w, 3.2,
    "How the tiers differ: the controls are the same for both. Essential entities face proactive supervision and fines up to "
    "EUR 10M or 2% of global turnover; important entities face ex-post supervision and fines up to EUR 7M or 1.4%. "
    "Management can be held personally liable in both tiers.")
pdf.ln(1)

y = pdf.get_y()
pdf.set_draw_color(*BLUE)
pdf.set_line_width(0.5)
pdf.line(11, y, 11 + page_w, y)
pdf.ln(1.4)
pdf.set_font("Helvetica", "", 8)
pdf.set_text_color(*DARK)
pdf.write(3.8, 'Scored mostly "No" in any section? That is what a gap assessment is for.  ')
pdf.set_font("Helvetica", "B", 8)
pdf.set_text_color(*NAVY)
pdf.write(3.8, "Tenny Vongtip - NIS2 Compliance Auditor & Zero Trust Architect  ·  GIAC-certified (8 domains)  ·  tennyv.com  ·  tenny.vongtip@gmail.com")

pdf.output("nis2-checklist.pdf")
print(f"pages: {pdf.pages_count}, ended at y={pdf.get_y():.0f}mm of 297mm")
