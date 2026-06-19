from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUTPUT = "files/brian-mak-public-profile.pdf"


def build_pdf():
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "Title",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=26,
        textColor=colors.HexColor("#1a2a3a"),
        spaceAfter=10,
    )
    subtitle = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#666666"),
        spaceAfter=16,
    )
    section = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#1a2a3a"),
        spaceBefore=12,
        spaceAfter=6,
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor("#333333"),
        spaceAfter=6,
    )
    bullet = ParagraphStyle(
        "Bullet",
        parent=body,
        leftIndent=14,
        firstLineIndent=-8,
    )

    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=letter,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
    )

    story = [
        Paragraph("Brian Mak", title),
        Paragraph(
            "French Language Specialist | University of Manitoba French Major",
            subtitle,
        ),
        Paragraph("Professional Summary", section),
        Paragraph(
            "Brian is a French language specialist with an Advanced Major in French "
            "and international tutoring and teaching experience in Canada, Hong Kong, "
            "and Ukraine. He has experience in one-on-one and small-group instruction, "
            "lesson planning, grammar, pronunciation, and conversation coaching for "
            "beginner to intermediate learners.",
            body,
        ),
        Paragraph("Teaching & Language Skills", section),
        Paragraph("- French instruction for beginner to intermediate learners", bullet),
        Paragraph("- One-on-one and small-group tutoring", bullet),
        Paragraph("- Lesson planning, grammar, pronunciation, and conversation coaching", bullet),
        Paragraph("- Student-centred and communicative teaching approach", bullet),
        Paragraph("Languages", section),
        Paragraph("- Cantonese and Mandarin: native", bullet),
        Paragraph("- English and French: fluent", bullet),
        Paragraph("- Russian: intermediate; Spanish and Ukrainian: basic", bullet),
        Paragraph("Relevant Teaching Experience", section),
    ]

    experience = [
        [
            Paragraph("<b>French Tutor/Instructor</b><br/>University of Manitoba, Canada", body),
            Paragraph("Tutored students at varying proficiency levels and created customized lessons focused on grammar, vocabulary, conversation, exam preparation, and academic coursework.", body),
        ],
        [
            Paragraph("<b>Private English Tutor</b><br/>Hong Kong", body),
            Paragraph("Delivered one-on-one instruction for students of different ages, strengthening communication skills, grammar, and confidence in spoken English.", body),
        ],
        [
            Paragraph("<b>ESL Instructor</b><br/>Olympic College named after Ivan Piddubnyi, Ukraine", body),
            Paragraph("Delivered ESL instruction to athletes and college staff in group settings.", body),
        ],
    ]
    table = Table(experience, colWidths=[2.1 * inch, 4.4 * inch], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ("LINEBELOW", (0, 0), (-1, -2), 0.25, colors.HexColor("#dddddd")),
            ]
        )
    )
    story.append(table)
    story += [
        Spacer(1, 8),
        Paragraph("Education", section),
        Paragraph("- Bachelor of Arts, Advanced Major in French, Minor in Russian - University of Manitoba", bullet),
        Paragraph("- Diploma in Hospitality Management - Vancouver Community College", bullet),
        Spacer(1, 12),
        Paragraph(
            "TalentU French | #200 - 5000 Kingsway, Burnaby, BC | talentufrench.ca",
            ParagraphStyle(
                "Footer",
                parent=styles["Normal"],
                fontSize=9,
                leading=12,
                textColor=colors.HexColor("#666666"),
                alignment=1,
            ),
        ),
    ]

    doc.build(story)


if __name__ == "__main__":
    build_pdf()
