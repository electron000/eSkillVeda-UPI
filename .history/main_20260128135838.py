from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse

app = FastAPI(title="eSkillVeda UPI Payment Page")

# -------------------------------
# Health check endpoint for UptimeRobot
# -------------------------------
@app.get("/health", response_class=PlainTextResponse)
methods=["GET", "HEAD"],
def health():
    return "OK"

# -------------------------------
# Existing code (UNCHANGED)
# -------------------------------

# Fixed fee amount
AMOUNT = "2500.00"

# UPI Deep Link Construction
UPI_LINK = (
    "upi://pay?"
    "pa=eskillvedaedtech@sbi"
    "&pn=ESKILLVEDA%20EDTECH%20PRIVATE%20LIMITED"
    "&mc=8241"
    "&tr="
    "&tn=Course%20Fee"
    f"&am={AMOUNT}"
    "&cu=INR"
    "&url="
    "&mode=02"
    "&purpose=00"
    "&orgid=180102"
    "&sign=MEUCIAhR03oQ2uuXEMl+huknYjM6dU9XsbTaD2Zl/EEnbTgtAiEA2iZbD7gGOqVHeUOvk98mNRSkCu7CgHLkT6CKM8USGzk="
)

@app.get("/pay", response_class=HTMLResponse)
def pay():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>eSkillVeda Payment</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background: #ffffff;
                font-family: 'Segoe UI', Arial, sans-serif;
            }}
            .container {{
                text-align: center;
                width: 100%;
                max-width: 340px;
                padding: 30px 20px;
                /* Optional: Add a subtle shadow for a 'card' feel */
                box-shadow: 0 4px 15px rgba(0,0,0,0.05);
                border-radius: 12px;
                border: 1px solid #f0f0f0;
            }}
            /* New Logo Styles */
            .logo {{
                font-size: 32px;
                font-weight: 800;
                margin-bottom: 25px;
                letter-spacing: -0.5px;
                line-height: 1.2;
            }}
            .text-yellow {{
                color: #f9a825; /* Matches previous loader yellow */
            }}
            .text-blue {{
                color: #1e88e5; /* Matches previous loader blue */
            }}
            
            .title {{
                font-size: 18px;
                font-weight: 500;
                color: #555;
                margin-bottom: 8px;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            .amount {{
                font-size: 36px;
                font-weight: 700;
                color: #222;
                margin-bottom: 25px;
            }}
            .currency {{
                font-size: 24px;
                color: #555;
                vertical-align: top;
                margin-top: 4px;
                display: inline-block;
            }}
            .btn {{
                display: block;
                width: 100%;
                box-sizing: border-box;
                padding: 16px;
                font-size: 18px;
                background: #1e88e5;
                color: white;
                border-radius: 8px;
                text-decoration: none;
                font-weight: 600;
                transition: background 0.2s;
                box-shadow: 0 4px 6px rgba(30, 136, 229, 0.2);
            }}
            .btn:hover {{
                background: #1976d2;
            }}
            .hint {{
                margin-top: 15px;
                font-size: 14px;
                color: #777;
                line-height: 1.4;
            }}
            .brand-footer {{
                margin-top: 30px;
                font-size: 12px;
                color: #aaa;
                border-top: 1px solid #eee;
                padding-top: 15px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">
                <span class="text-yellow">e</span><span class="text-blue">SkillVeda</span>
            </div>

            <div class="title">Total Payable</div>
            
            <div class="amount">
                <span class="currency">₹</span>2,500
            </div>

            <a class="btn" href="{UPI_LINK}">
                Pay Securely
            </a>

            <div class="hint">
                Tap the button above to pay using GPay, PhonePe, or Paytm.
            </div>

            <div class="brand-footer">
                Secured by eSkillVeda Payments
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)