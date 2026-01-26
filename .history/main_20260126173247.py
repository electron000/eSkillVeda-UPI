from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="eSkillVeda UPI Redirect Service")

UPI_LINK = "upi://pay?pa=eskillvedaedtech@sbi&pn=ESKILLVEDA%20EDTECH%20PRIVATE%20LIMITED&mc=8241&tr=&tn=&am=&cu=INR&url=&mode=02&purpose=00&orgid=180102&sign=MEUCIAhR03oQ2uuXEMl+huknYjM6dU9XsbTaD2Zl/EEnbTgtAiEA2iZbD7gGOqVHeUOvk98mNRSkCu7CgHLkT6CKM8USGzk="

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
                font-family: Arial, sans-serif;
            }}
            .container {{
                text-align: center;
                width: 100%;
                max-width: 300px;
            }}
            .loader {{
                width: 70px;
                height: 70px;
                border: 6px solid #f1f1f1;
                border-top: 6px solid #1e88e5;
                border-right: 6px solid #f9a825;
                border-radius: 50%;
                animation: spin 1s linear infinite;
                margin: 0 auto 20px;
            }}
            @keyframes spin {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}
            .text {{
                font-size: 18px;
                color: #333;
                font-weight: 500;
                margin-bottom: 16px;
            }}
            .btn {{
                display: inline-block;
                padding: 12px 20px;
                font-size: 16px;
                background: #1e88e5;
                color: white;
                border-radius: 6px;
                text-decoration: none;
                font-weight: 600;
            }}
            .hint {{
                margin-top: 12px;
                font-size: 13px;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="loader"></div>
            <div class="text">Continue to payment</div>

            <a class="btn" href="{UPI_LINK}">
                Open Payment App
            </a>

            <div class="hint">
                If it does not open automatically, tap the button.
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)