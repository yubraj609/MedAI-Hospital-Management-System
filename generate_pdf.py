import sys
import subprocess

try:
    import reportlab
except ImportError:
    print("Installing reportlab...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    import reportlab

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

def build_pdf(filename="MediAI_System_Architecture_and_Modules.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom Palette
    PRIMARY = colors.HexColor("#1e3a8a")   # Deep Blue
    SECONDARY = colors.HexColor("#0284c7") # Sky Blue
    ACCENT = colors.HexColor("#0f766e")    # Teal
    DARK_TEXT = colors.HexColor("#1f2937") # Charcoal
    BG_LIGHT = colors.HexColor("#f8fafc")  # Off-white
    BORDER_COLOR = colors.HexColor("#cbd5e1") # Slate border

    # Custom Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=PRIMARY,
        alignment=TA_CENTER,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=SECONDARY,
        alignment=TA_CENTER,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=PRIMARY,
        spaceBefore=14,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=ACCENT,
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=DARK_TEXT,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=body_style,
        leftIndent=12,
        spaceAfter=4
    )

    tbl_header_style = ParagraphStyle(
        'TblHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.white,
        alignment=TA_LEFT
    )

    tbl_cell_style = ParagraphStyle(
        'TblCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=DARK_TEXT
    )

    story = []

    # Title & Header
    story.append(Paragraph("MediAI — Hospital Management System", title_style))
    story.append(Paragraph("Technical Architecture, Technology Stack & Module Specification Report", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceAfter=12))

    # 1. Architecture Overview
    story.append(Paragraph("1. System Architecture Overview", h1_style))
    story.append(Paragraph(
        "MediAI is a full-stack, enterprise-grade medical management platform designed with a <b>3-Tier Microservices / Service-Oriented Architecture</b>. "
        "The system decouples the frontend client, core backend REST API services, and AI computation engine into specialized, independently scalable components:",
        body_style
    ))
    story.append(Paragraph("• <b>Frontend Client Layer:</b> Single Page Application (SPA) built with React 18 & Vite, featuring role-based dashboards.", bullet_style))
    story.append(Paragraph("• <b>Backend API Layer:</b> Node.js & Express RESTful API server handling authentication, RBAC, business logic, and communications.", bullet_style))
    story.append(Paragraph("• <b>AI Microservice Layer:</b> FastAPI Python service providing intelligent symptom checking, lab report summarization, and medical chatbot assistance.", bullet_style))
    story.append(Paragraph("• <b>Database Layer:</b> MongoDB document store with Mongoose ODM and embedded in-memory database support for zero-dependency execution.", bullet_style))
    story.append(Spacer(1, 8))

    # 2. Frontend Layer
    story.append(Paragraph("2. Frontend Layer (Client)", h1_style))
    story.append(Paragraph("<b>Technologies & Libraries Used:</b>", h2_style))

    fe_tech_data = [
        [Paragraph("Technology", tbl_header_style), Paragraph("Version", tbl_header_style), Paragraph("Purpose / Architectural Role", tbl_header_style)],
        [Paragraph("React", tbl_cell_style), Paragraph("^18.3.1", tbl_cell_style), Paragraph("Component-driven UI rendering engine", tbl_cell_style)],
        [Paragraph("React DOM", tbl_cell_style), Paragraph("^18.3.1", tbl_cell_style), Paragraph("DOM rendering binding for React", tbl_cell_style)],
        [Paragraph("React Router DOM", tbl_cell_style), Paragraph("^6.28.0", tbl_cell_style), Paragraph("Declarative client-side routing & route protection", tbl_cell_style)],
        [Paragraph("Vite", tbl_cell_style), Paragraph("^5.4.10", tbl_cell_style), Paragraph("Next-generation frontend toolchain & dev server", tbl_cell_style)],
        [Paragraph("CSS3", tbl_cell_style), Paragraph("Native", tbl_cell_style), Paragraph("Custom design system using CSS Variables (styles.css)", tbl_cell_style)]
    ]
    fe_table = Table(fe_tech_data, colWidths=[110, 60, 350])
    fe_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, BG_LIGHT]),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR)
    ]))
    story.append(fe_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Frontend Modules & Feature Workspaces:</b>", h2_style))
    fe_modules = [
        ("Dashboard Module", "Live KPI tracking for revenue, active doctors, total patients, system health, and department coverage."),
        ("Dynamic Auth & Role Switcher", "Dynamic sidebar navigation tailored to user roles (Admin, Doctor, Patient)."),
        ("Doctor Directory Module", "Registration form and table to manage doctors, departments, experience, availability, and consultation fees."),
        ("Appointments & Booking Module", "Appointment scheduling and tracking for patients and doctors (Confirmed, Pending, Completed)."),
        ("Patient Records & Detail View", "Comprehensive demographic tracking, medical history notes, and active treatment plans."),
        ("Prescription Management Module", "Prescription creation tool and formatted printable output view (PrintablePrescriptionPage)."),
        ("Lab Reports Module", "Pathology lab result tracking (CBC, ECG, Liver Function, Blood Sugar) with notes."),
        ("Billing & Invoicing Module", "Invoice manager with total revenue calculation, payment modes (Card, UPI), and status tracking."),
        ("Inventory Management Module", "Pharmacy and medical equipment stock control with expiry tracking."),
        ("Staff Management Module", "Hospital workforce tracking across departments (Nurses, Receptionists, Technicians)."),
        ("Interactive Calendar Module", "Weekly shift schedule board with drag-and-drop support for doctor rounds."),
        ("AI Assistant Interface", "Interactive workspace for symptom checking and medical report analysis."),
        ("Alerts & Notification Hub", "SMS/Email alert dispatcher and audit log viewer."),
        ("Reports & Export Module", "Operational performance analytics charts with CSV download and print capabilities.")
    ]
    for name, desc in fe_modules:
        story.append(Paragraph(f"• <b>{name}:</b> {desc}", bullet_style))
    story.append(Spacer(1, 8))

    # 3. Backend Layer
    story.append(Paragraph("3. Backend Layer (Server)", h1_style))
    story.append(Paragraph("<b>Technologies & Libraries Used:</b>", h2_style))

    be_tech_data = [
        [Paragraph("Technology", tbl_header_style), Paragraph("Version", tbl_header_style), Paragraph("Purpose / Architectural Role", tbl_header_style)],
        [Paragraph("Node.js", tbl_cell_style), Paragraph("Runtime", tbl_cell_style), Paragraph("Asynchronous server-side JavaScript runtime", tbl_cell_style)],
        [Paragraph("Express.js", tbl_cell_style), Paragraph("^4.21.1", tbl_cell_style), Paragraph("RESTful API framework & routing engine", tbl_cell_style)],
        [Paragraph("jsonwebtoken", tbl_cell_style), Paragraph("^9.0.2", tbl_cell_style), Paragraph("Stateless JWT authentication & token signing", tbl_cell_style)],
        [Paragraph("bcryptjs", tbl_cell_style), Paragraph("^2.4.3", tbl_cell_style), Paragraph("Secure password hashing and comparison", tbl_cell_style)],
        [Paragraph("Nodemailer", tbl_cell_style), Paragraph("^7.0.0", tbl_cell_style), Paragraph("SMTP mail dispatching for email alerts", tbl_cell_style)],
        [Paragraph("Twilio SDK", tbl_cell_style), Paragraph("^5.7.1", tbl_cell_style), Paragraph("SMS notification service integration", tbl_cell_style)],
        [Paragraph("CORS", tbl_cell_style), Paragraph("^2.8.5", tbl_cell_style), Paragraph("Cross-Origin Resource Sharing handling", tbl_cell_style)],
        [Paragraph("dotenv", tbl_cell_style), Paragraph("^16.4.5", tbl_cell_style), Paragraph("Environment variable configuration loader", tbl_cell_style)]
    ]
    be_table = Table(be_tech_data, colWidths=[110, 60, 350])
    be_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, BG_LIGHT]),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR)
    ]))
    story.append(be_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Backend Modules & REST API Services:</b>", h2_style))
    be_modules = [
        ("Authentication Module", "Endpoints: POST /api/auth/register, POST /api/auth/login, GET /api/auth/profile."),
        ("RBAC & Security Middleware", "authenticateToken and authorizeRoles middleware enforcing endpoint access control."),
        ("Dashboard Aggregation Service", "GET /api/dashboard — calculates total patients, active doctors, revenue ($group aggregation), and pending bills."),
        ("Hospital CRUD APIs", "Dedicated REST endpoints for /api/patients, /api/doctors, /api/appointments, /api/billing, /api/lab-reports, /api/inventory, /api/staff."),
        ("Communication Gateway", "POST /api/notifications/send — multi-channel notification engine (SMTP Email & Twilio SMS)."),
        ("Automated Seeding System", "Initializes database with default admin users, doctors, patients, billing, inventory, and staff records on launch.")
    ]
    for name, desc in be_modules:
        story.append(Paragraph(f"• <b>{name}:</b> {desc}", bullet_style))
    story.append(Spacer(1, 8))

    # 4. AI Microservice Layer
    story.append(Paragraph("4. AI Microservice Layer", h1_style))
    story.append(Paragraph("<b>Technologies Used:</b> Python 3, FastAPI, Uvicorn, Pydantic.", body_style))
    story.append(Paragraph("<b>AI Microservice Modules:</b>", h2_style))
    ai_modules = [
        ("Symptom Checker Service (POST /symptom-checker)", "Evaluates user symptoms, determines risk level (low/medium), and suggests possible non-diagnostic conditions."),
        ("Report Summarizer Service (POST /report-summary)", "Parses lab test reports (blood sugar, ECG, general tests) and generates plain-language summaries."),
        ("Medical Chatbot Service (POST /chatbot)", "Conversational AI assistant answering patient queries regarding appointments, prescriptions, and timings."),
        ("Service Health Endpoint (GET /health)", "Microservice heartbeat monitoring.")
    ]
    for name, desc in ai_modules:
        story.append(Paragraph(f"• <b>{name}:</b> {desc}", bullet_style))
    story.append(Spacer(1, 8))

    # 5. Database Layer
    story.append(Paragraph("5. Database Layer", h1_style))
    story.append(Paragraph("<b>Technologies Used:</b> MongoDB (NoSQL Document Store), Mongoose ODM (^8.8.0), MongoMemoryServer (^11.2.0).", body_style))
    story.append(Paragraph("<b>Database Models & Entities:</b>", h2_style))

    db_models_data = [
        [Paragraph("Model", tbl_header_style), Paragraph("Key Fields / Attributes", tbl_header_style), Paragraph("Description", tbl_header_style)],
        [Paragraph("User", tbl_cell_style), Paragraph("name, email, password (hashed), role", tbl_cell_style), Paragraph("Authentication & RBAC accounts", tbl_cell_style)],
        [Paragraph("Doctor", tbl_cell_style), Paragraph("name, department, experience, status, fees", tbl_cell_style), Paragraph("Doctor profile & consultation data", tbl_cell_style)],
        [Paragraph("Patient", tbl_cell_style), Paragraph("patientId, name, age, gender, phone, condition", tbl_cell_style), Paragraph("Patient demographics & medical profile", tbl_cell_style)],
        [Paragraph("Billing", tbl_cell_style), Paragraph("invoiceNo, patientName, amount, status, paymentMode", tbl_cell_style), Paragraph("Hospital invoices & revenue records", tbl_cell_style)],
        [Paragraph("LabReport", tbl_cell_style), Paragraph("reportId, patientName, tests, status, notes", tbl_cell_style), Paragraph("Pathology lab test data", tbl_cell_style)],
        [Paragraph("InventoryItem", tbl_cell_style), Paragraph("name, category, stock, price, expiry", tbl_cell_style), Paragraph("Pharmacy & medical equipment stock", tbl_cell_style)],
        [Paragraph("Staff", tbl_cell_style), Paragraph("name, role, department, email, status", tbl_cell_style), Paragraph("Hospital workforce records", tbl_cell_style)]
    ]
    db_table = Table(db_models_data, colWidths=[90, 220, 210])
    db_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, BG_LIGHT]),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR)
    ]))
    story.append(db_table)
    story.append(Spacer(1, 14))

    # Summary Footer
    story.append(HRFlowable(width="100%", thickness=1, color=SECONDARY, spaceAfter=8))
    story.append(Paragraph("MediAI Hospital Management System — Generated Architecture & Module Report", ParagraphStyle(
        'FooterText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        textColor=colors.HexColor("#64748b"),
        alignment=TA_CENTER
    )))

    doc.build(story)
    print(f"Successfully generated PDF: {filename}")

if __name__ == "__main__":
    out = "MediAI_System_Architecture_and_Modules.pdf"
    if len(sys.argv) > 1:
        out = sys.argv[1]
    build_pdf(out)
