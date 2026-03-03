import streamlit as st
from PIL import Image
import base64

try:
    im= Image.open("assets/logo.png")
except FileNotFoundError:
    im = None
st.set_page_config(layout="wide", page_title="Sriram Sai | Portfolio", page_icon=im)

def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

img_b64 = img_to_base64("assets/NANII.png")

bg_b64 = img_to_base64("assets/sky.jpg")


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@400;500&family=Cormorant+Garamond:wght@400;600;700&family=Inter:wght@300;400;500;600&family=Montserrat:wght@300;400;600;700&family=Share+Tech+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Inter:wght@300;400;500;600&family=Montserrat:wght@300;400;600;700&family=Share+Tech+Mono&display=swap');
:root { --gold:#b8860b; --gold2:#d4a017; --gold3:#f0c040; --cream:#fdfcf7; --muted:#a09070; }
footer,#MainMenu,header,[data-testid="stSidebar"],[data-testid="collapsedControl"],[data-testid="stDecoration"]{display:none!important;}
#particle-canvas{position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:-1;}
html,body,[data-testid="stAppViewContainer"]{background:transparent!important;color:var(--cream)!important;font-family:'Montserrat',sans-serif!important;}
/* galaxy bg applied via JS below */
#galaxy-overlay{position:fixed;inset:0;z-index:-1;pointer-events:none;background:radial-gradient(ellipse at 20% 20%,rgba(184,134,11,0.08) 0%,transparent 40%),radial-gradient(ellipse at 80% 80%,rgba(80,40,120,0.10) 0%,transparent 40%),rgba(5,4,12,0.85);}
[data-testid="stAppViewContainer"]{background:transparent!important;min-height:100vh!important;position:relative!important;}
.glow-orb{position:fixed;border-radius:50%;pointer-events:none;z-index:0;filter:blur(80px);opacity:0.18;animation:orb-float 12s ease-in-out infinite;}
.glow-orb-1{width:500px;height:500px;background:radial-gradient(circle,#d4a017 0%,#b8860b 40%,transparent 70%);top:-100px;left:-100px;animation-duration:14s;}
.glow-orb-2{width:400px;height:400px;background:radial-gradient(circle,#f0c040 0%,#b8860b 50%,transparent 70%);bottom:10%;right:-80px;animation-duration:18s;animation-delay:-6s;}
.glow-orb-3{width:300px;height:300px;background:radial-gradient(circle,#8b6508 0%,#5a3e05 50%,transparent 70%);top:40%;left:30%;animation-duration:22s;animation-delay:-10s;opacity:0.10;}
@keyframes orb-float{0%,100%{transform:translate(0,0) scale(1);}33%{transform:translate(30px,-40px) scale(1.08);}66%{transform:translate(-20px,30px) scale(0.95);}}
[data-testid="stAppViewContainer"]>section{padding-top:0!important;padding-left:0!important;padding-right:0!important;position:relative;z-index:1;}
.stMarkdown{padding:0!important;}
.stMarkdown>div{width:100%!important;}

/* ── NAVBAR ── */
.navbar{position:fixed;top:0;left:0;right:0;z-index:9999;background:rgba(10,8,4,0.88);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid rgba(184,134,11,0.2);display:flex;align-items:center;justify-content:space-between;padding:0 48px;height:62px;}
.nav-brand{font-family:'Cormorant Garamond',serif;font-size:1.15rem;font-weight:700;color:#fdfcf7!important;letter-spacing:2px;cursor:pointer;text-decoration:none!important;}
.nav-brand span{color:var(--gold2);}
.nav-links{display:flex;align-items:center;gap:2px;}
.nav-link{font-family:'Share Tech Mono',monospace;font-size:0.67rem;letter-spacing:1.5px;color:rgba(253,252,247,0.6)!important;text-decoration:none!important;padding:7px 14px;border-radius:4px;transition:all 0.25s;text-transform:uppercase;}
.nav-link:hover{color:var(--gold3)!important;background:rgba(184,134,11,0.1)!important;}
.nav-cta{font-family:'Share Tech Mono',monospace;font-size:0.65rem;letter-spacing:1.5px;color:#1a160e!important;text-decoration:none!important;background:var(--gold);padding:8px 20px;border-radius:4px;transition:all 0.25s;margin-left:10px;text-transform:uppercase;font-weight:700;}
.nav-cta:hover{background:var(--gold2);box-shadow:0 4px 20px rgba(184,134,11,0.45);}
/* ── BOTTOM NAVBAR (mobile only) ── */
.bot-nav{display:none;position:fixed;bottom:0;left:0;right:0;z-index:9999;background:rgba(5,4,12,0.95);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-top:1px solid rgba(184,134,11,0.2);height:62px;padding:0 4px;justify-content:space-around;align-items:center;}
.bot-nav-item{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;padding:6px 10px;border-radius:8px;text-decoration:none!important;color:rgba(253,252,247,0.45)!important;transition:all 0.2s;flex:1;min-width:0;}
.bot-nav-item:hover,.bot-nav-item.active{color:var(--gold)!important;}
.bot-nav-item.active .bot-nav-icon{filter:drop-shadow(0 0 4px var(--gold));}
.bot-nav-icon{font-size:1.15rem;line-height:1;}
.bot-nav-lbl{font-family:'Share Tech Mono',monospace;font-size:0.48rem;letter-spacing:1px;text-transform:uppercase;white-space:nowrap;}

/* ── LAYOUT ── */
.section{padding:80px 48px;max-width:1200px;margin:0 auto;}
.section-hero{padding:0 48px 80px;max-width:1200px;margin:0 auto;}
.gold-div{border:none;height:1px;background:linear-gradient(90deg,transparent,rgba(184,134,11,0.5),transparent);margin:0;}
.sec-eyebrow{font-family:'Share Tech Mono',monospace;font-size:0.65rem;color:var(--gold);letter-spacing:5px;text-transform:uppercase;margin-bottom:8px;display:flex;align-items:center;gap:12px;}
.sec-eyebrow::before{content:'';width:28px;height:1px;background:linear-gradient(90deg,var(--gold),var(--gold3));box-shadow:0 0 6px rgba(184,134,11,0.6);}

            
            
.sec-title{font-family:'Cormorant Garamond',serif;font-size:2.4rem;font-weight:700;color:#fdfcf7;line-height:1.15;margin-bottom:28px;}
.sec-title span{color:var(--gold);}

/* ── HERO ── */
.hero-wrap{display:flex;align-items:center;gap:48px;padding-top:10px;padding-bottom:60px;}
.hero-left{flex:1.6;} .hero-right{flex:1;display:flex;justify-content:flex-end;}
.hero-eyebrow{font-family:'Share Tech Mono',monospace;font-size:0.7rem;color:var(--gold);letter-spacing:5px;margin-bottom:18px;display:flex;align-items:center;gap:12px;}
.hero-eyebrow::before{content:'';width:36px;height:1px;background:var(--gold);box-shadow:0 0 8px var(--gold);}
.typewriter-text{font-family:'Share Tech Mono',monospace;font-size:0.7rem;color:var(--gold);letter-spacing:5px;text-transform:uppercase;overflow:hidden;border-right:2px solid var(--gold);white-space:nowrap;animation:typing 2.5s steps(22,end) forwards,blink 0.75s step-end infinite;width:0;}
@keyframes typing{from{width:0;}to{width:22ch;}} @keyframes blink{50%{border-color:transparent;}}
.hero-name{font-family:'Cormorant Garamond',serif;font-size:4rem;font-weight:700;color:#fdfcf7;line-height:1.05;letter-spacing:1px;margin-bottom:14px;animation:hero-fadein 1.2s ease 0.5s both;}
.hero-name span{color:var(--gold);}
.hero-role{font-size:0.85rem;font-weight:300;color:var(--muted);letter-spacing:3px;text-transform:uppercase;margin-bottom:22px;animation:hero-fadein 1.2s ease 0.8s both;}
.hero-desc{font-family:'Josefin Sans',sans-serif;font-size:0.95rem;font-weight:400;line-height:1.9;color:#dcd9f0;max-width:540px;margin-bottom:24px;animation:hero-fadein 1.2s ease 1s both;}
@keyframes hero-fadein{from{opacity:0;transform:translateY(18px);}to{opacity:1;transform:translateY(0);}}
.hero-photo-wrap{width:100%;max-width:420px;border-radius:14px;overflow:hidden;border:1px solid rgba(184,134,11,0.3);box-shadow:0 0 0 8px rgba(184,134,11,0.05),0 20px 60px rgba(0,0,0,0.5),0 0 40px rgba(184,134,11,0.1);transition:all 0.4s ease;animation:hero-fadein 1.4s ease 0.3s both;}
.hero-photo-wrap:hover{border-color:rgba(184,134,11,0.65);box-shadow:0 0 0 10px rgba(184,134,11,0.08),0 24px 70px rgba(0,0,0,0.6),0 0 60px rgba(184,134,11,0.18);transform:translateY(-6px);}
.hero-photo-wrap img{width:100%;height:auto;display:block;object-fit:cover;object-position:center top;}
.learn-strip{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:22px;}
.learn-lbl{font-family:'Share Tech Mono',monospace;font-size:0.6rem;color:var(--muted);letter-spacing:2px;}
.learn-tag{background:rgba(184,134,11,0.1);border:1px solid rgba(184,134,11,0.35);color:var(--gold3);padding:4px 14px;border-radius:20px;font-family:'Share Tech Mono',monospace;font-size:0.65rem;letter-spacing:1px;}
.kpi-strip{display:flex;gap:12px;flex-wrap:wrap;margin:22px 0 28px;}
.kpi-card{background:rgba(255,255,255,0.0);border:1px solid rgba(184,134,11,0.2);border-top:2px solid var(--gold);border-radius:8px;padding:14px 20px;text-align:center;min-width:100px;flex:1;transition:all 0.3s;backdrop-filter:blur(8px);}
.kpi-card:hover{transform:translateY(-4px);background:rgba(184,134,11,0.08);box-shadow:0 8px 24px rgba(184,134,11,0.15);}
.kpi-num{font-family:'Cormorant Garamond',serif;font-size:1.9rem;font-weight:700;color:var(--gold);line-height:1;}
.kpi-lbl{font-family:'Share Tech Mono',monospace;font-size:0.58rem;color:var(--muted);letter-spacing:2px;margin-top:5px;}
.dl-btn{display:inline-flex;align-items:center;gap:8px;background:var(--gold);color:#1a160e!important;text-decoration:none!important;font-family:'Share Tech Mono',monospace;font-size:0.75rem;letter-spacing:2px;font-weight:700;padding:12px 28px;border-radius:4px;box-shadow:0 4px 20px rgba(184,134,11,0.3);transition:all 0.3s;text-transform:uppercase;}
.dl-btn:hover{background:var(--gold2);box-shadow:0 6px 28px rgba(184,134,11,0.5);transform:translateY(-2px);}

/* ── ABOUT ── */
.about-text{font-family:'Inter',sans-serif;font-size:0.97rem;font-weight:400;font-style:normal;line-height:1.95;color:rgba(220,225,240,0.82);margin-bottom:28px;letter-spacing:0.1px;}
.about-text strong{font-style:normal;color:#fdfcf7;font-weight:600;}
.about-highlight{font-family:'Inter',sans-serif;font-size:0.95rem;font-style:normal;font-weight:500;color:var(--gold3);margin:18px 0 24px;padding-left:16px;border-left:2px solid var(--gold);line-height:1.8;}
.trait-chip{display:inline-block;background:rgba(184,134,11,0.08);border:1px solid rgba(184,134,11,0.25);color:var(--gold3);padding:6px 18px;border-radius:4px;font-family:'Share Tech Mono',monospace;font-size:0.67rem;margin:5px;letter-spacing:1px;}

/* ── INFO CARDS ── */
.info-card{background:rgba(255,255,255,0.0);border:1px solid rgba(184,134,11,0.12);border-left:3px solid var(--gold);border-radius:8px;padding:18px 22px;margin-bottom:12px;transition:all 0.25s;backdrop-filter:blur(4px);}
.info-card:hover{background:rgba(184,134,11,0.05);border-left-color:var(--gold2);transform:translateX(4px);box-shadow:0 4px 20px rgba(184,134,11,0.1);}
.ic-title{font-family:'Inter',sans-serif;font-weight:600;font-size:1rem;color:#e8ecf4;margin-bottom:4px;}
.ic-sub{font-family:'Inter',sans-serif;font-style:normal;font-size:0.85rem;color:rgba(180,190,210,0.8);margin-bottom:5px;}
.ic-detail{font-family:'Share Tech Mono',monospace;font-size:0.68rem;color:var(--gold);letter-spacing:1px;}

/* ── SKILLS ── */
.skill-group-title{font-family:'Share Tech Mono',monospace;font-size:0.7rem;color:var(--gold);letter-spacing:2px;margin-bottom:16px;padding-bottom:8px;border-bottom:1px solid rgba(184,134,11,0.2);}
.skill-wrap{margin-bottom:28px;}
.skill-row{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;}
.skill-name{display:flex;align-items:center;gap:10px;font-size:0.92rem;font-weight:500;color:rgba(253,252,247,0.9);}
.skill-icon{font-size:1.1rem;width:24px;text-align:center;}
.skill-pct{font-family:'Share Tech Mono',monospace;font-size:0.75rem;color:var(--gold);}
.skill-track{background:rgba(255,255,255,0.06);border-radius:20px;height:8px;overflow:hidden;}
.skill-fill{height:100%;background:linear-gradient(90deg,#b8860b,#f0c040,#ffe680);border-radius:20px;box-shadow:0 0 14px rgba(240,192,64,0.55);animation:bar-grow 1.4s cubic-bezier(0.25,1,0.5,1) both;}
@keyframes bar-grow{from{transform:scaleX(0);transform-origin:left;}to{transform:scaleX(1);transform-origin:left;}}

/* ── CERTS ── */
.cert-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px;}
.cert-card{background:rgba(255,255,255,0.0);border:1px solid rgba(184,134,11,0.12);border-radius:12px;padding:28px 24px;transition:all 0.3s;backdrop-filter:blur(4px);position:relative;overflow:hidden;min-height:180px;}
.cert-card::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--gold),transparent);opacity:0;transition:opacity 0.3s;}
.cert-card:hover{background:rgba(184,134,11,0.06);border-color:rgba(184,134,11,0.35);transform:translateY(-6px);box-shadow:0 14px 36px rgba(184,134,11,0.15);}
.cert-card:hover::after{opacity:1;}
.cert-icon{font-size:2rem;margin-bottom:14px;}
.cert-name{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:1.05rem;color:#fdfcf7;line-height:1.4;margin-bottom:6px;}
.cert-issuer{font-family:'Share Tech Mono',monospace;font-size:0.65rem;color:var(--gold);letter-spacing:1.5px;}
.cert-badge{display:inline-block;margin-top:14px;background:rgba(74,222,128,0.1);border:1px solid rgba(74,222,128,0.25);color:#4ade80;font-family:'Share Tech Mono',monospace;font-size:0.6rem;padding:3px 10px;border-radius:10px;}

/* ── PROJECT CARDS ── */
.proj-grid{display:grid!important;grid-template-columns:repeat(3,1fr)!important;gap:20px;width:100%;}
.proj-card{background:rgba(15,12,6,0.85);border:1px solid rgba(184,134,11,0.15);border-radius:16px!important;overflow:hidden!important;display:flex;flex-direction:column;transition:all 0.4s cubic-bezier(0.34,1.2,0.64,1);position:relative;}
.proj-card::before{content:'';position:absolute;left:0;top:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--gold),transparent);transform:scaleX(0);transform-origin:left;transition:transform 0.4s;z-index:2;}
.proj-card:hover{border-color:rgba(184,134,11,0.35);transform:translateY(-6px);box-shadow:0 20px 50px rgba(0,0,0,0.5),0 0 40px rgba(184,134,11,0.1);}
.proj-card:hover::before{transform:scaleX(1);}
.proj-preview{width:100%;height:210px;overflow:hidden;position:relative;border-bottom:1px solid rgba(184,134,11,0.15);background:#080604;flex-shrink:0;border-radius:16px 16px 0 0;}
.proj-preview img{width:100%;height:100%;object-fit:cover;object-position:top center;display:block;transition:transform 0.4s ease;}
.proj-card:hover .proj-preview img{transform:scale(1.04);}
.proj-preview-overlay{position:absolute;inset:0;background:linear-gradient(to bottom,transparent 45%,rgba(10,8,4,0.85) 100%);z-index:1;}
.proj-preview-placeholder{width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;background:linear-gradient(135deg,rgba(184,134,11,0.1) 0%,rgba(10,8,4,0.95) 100%);gap:10px;}
.proj-card-body{padding:18px 22px 20px 22px;display:flex;flex-direction:column;flex:1;}
.proj-num{font-family:'Share Tech Mono',monospace;font-size:0.65rem;color:var(--gold);letter-spacing:3px;margin-bottom:8px;}
.proj-title{font-family:'Cormorant Garamond',serif;font-size:1.2rem;font-weight:700;color:#fdfcf7;margin-bottom:10px;line-height:1.3;}
.proj-desc{font-family:'Inter',sans-serif;font-style:normal;font-weight:400;font-size:0.82rem;line-height:1.75;color:rgba(210,218,235,0.75);margin-bottom:14px;flex:1;}
.tech-badge{display:inline-block;background:rgba(184,134,11,0.10);border:1px solid rgba(240,192,64,0.25);color:#ffe680;padding:3px 10px;border-radius:20px;font-size:0.65rem;margin:3px;font-family:'Share Tech Mono',monospace;letter-spacing:0.5px;}
.feat-badge{font-family:'Share Tech Mono',monospace;font-size:0.58rem;letter-spacing:2px;background:rgba(184,134,11,0.1);border:1px solid var(--gold);color:var(--gold3);padding:3px 10px;border-radius:20px;animation:feat-pulse 2.5s ease-in-out infinite;}
@keyframes feat-pulse{0%,100%{opacity:1;}50%{opacity:0.5;}}
.proj-link{display:inline-flex;align-items:center;gap:6px;background:transparent;color:var(--gold)!important;text-decoration:none!important;padding:9px 20px;border-radius:4px;border:1px solid rgba(184,134,11,0.4);font-family:'Share Tech Mono',monospace;font-size:0.7rem;letter-spacing:1px;font-weight:700;transition:all 0.25s;margin-top:14px;align-self:flex-start;}
.proj-link:hover{background:var(--gold);color:#1a160e!important;box-shadow:0 6px 22px rgba(184,134,11,0.35);transform:translateY(-2px);}

/* ── CONTACT ── */
.c-form input,.c-form textarea{width:100%;background:rgba(0,0,0,0.0)!important;border:1px solid rgba(184,134,11,0.2)!important;border-radius:6px!important;color:#fdfcf7!important;font-family:'Montserrat',sans-serif!important;font-size:0.9rem!important;padding:12px 16px!important;margin-bottom:12px!important;outline:none!important;box-sizing:border-box!important;transition:border-color 0.25s!important;}
.c-form input::placeholder,.c-form textarea::placeholder{color:var(--muted)!important;}
.c-form input:focus,.c-form textarea:focus{border-color:var(--gold)!important;box-shadow:0 0 12px rgba(184,134,11,0.15)!important;background:rgba(184,134,11,0.06)!important;}
.c-form textarea{min-height:130px;resize:vertical;}
.c-form button{background:var(--gold)!important;color:#1a160e!important;border:none!important;padding:12px 28px!important;border-radius:4px!important;font-family:'Share Tech Mono',monospace!important;font-size:0.78rem!important;letter-spacing:2px!important;font-weight:700!important;cursor:pointer!important;transition:all 0.25s!important;box-shadow:0 4px 16px rgba(184,134,11,0.25)!important;}
.c-form button:hover{background:var(--gold2)!important;box-shadow:0 6px 24px rgba(184,134,11,0.45)!important;}
.soc-btn{display:inline-flex;align-items:center;gap:8px;padding:10px 20px;border-radius:6px;font-family:'Share Tech Mono',monospace;font-size:0.7rem;letter-spacing:1.5px;text-decoration:none!important;transition:all 0.25s;border:1px solid rgba(184,134,11,0.18);background:rgba(255,255,255,0.0);color:rgba(253,252,247,0.75)!important;margin-bottom:8px;width:100%;}
.soc-btn:hover{background:rgba(184,134,11,0.08);border-color:rgba(184,134,11,0.4);color:var(--gold3)!important;transform:translateX(4px);}
.footer{text-align:center;padding:32px 0 20px;border-top:1px solid rgba(184,134,11,0.15);font-family:'Share Tech Mono',monospace;font-size:0.67rem;color:var(--muted);letter-spacing:2px;}
.footer a{color:var(--gold);text-decoration:none;}
::-webkit-scrollbar{width:5px;}
::-webkit-scrollbar-track{background:#0f0c06;}
::-webkit-scrollbar-thumb{background:var(--gold);border-radius:3px;}


/* Large Tablets & Small Laptops (1024px and below) */
@media(max-width:1024px){
    .proj-grid{grid-template-columns:repeat(2,1fr)!important;}
    .hero-wrap{gap:32px;}
    .hero-name{font-size:3.2rem;}
    .hero-photo-wrap{max-width:340px;}
    .section,.section-hero{padding-left:32px;padding-right:32px;}
    .navbar{padding:0 32px;}
}

/* Tablets (768px and below) */
@media(max-width:768px){
    /* Hero Section - Stack vertically */
    .hero-wrap{flex-direction:column-reverse;padding-top:20px;text-align:center;}
    .hero-left{width:100%;}
    .hero-right{width:100%;justify-content:center;margin-bottom:32px;}
    .hero-name{font-size:2.8rem;}
    .hero-role{font-size:0.75rem;}
    .hero-desc{font-size:0.9rem;max-width:100%;padding:0 10px;}
    .hero-photo-wrap{max-width:280px;width:80%;margin:0 auto;}
    .hero-photo-wrap img{width:100%;height:auto;}

    /* Typography */
    .sec-title{font-size:2rem;}
    .sec-eyebrow{font-size:0.6rem;}

    /* Navigation */
    .navbar{padding:0 16px;height:56px;}
    .nav-brand{font-size:1rem;}
    .nav-links{display:none;}
    .nav-cta{display:none;}
    .bot-nav{display:flex;}
    /* extra bottom padding so content isn't hidden behind bottom nav */
    .footer{padding-bottom:80px;}
    .section{padding-bottom:80px;}

    /* Layout */
    .section,.section-hero{padding-left:20px;padding-right:20px;padding-top:60px;padding-bottom:60px;}

    /* Projects Grid */
    .proj-grid{grid-template-columns:1fr!important;gap:16px;}
    .proj-preview{height:180px;}
    .proj-title{font-size:1.1rem;}
    .proj-desc{font-size:0.8rem;}

    /* Certs Grid */
    .cert-grid{grid-template-columns:1fr;}

    /* KPI Cards */
    .kpi-strip{gap:8px;justify-content:center;}
    .kpi-card{min-width:70px;padding:10px 8px;flex:0 1 calc(25% - 8px);}
    .kpi-num{font-size:1.4rem;}
    .kpi-lbl{font-size:0.5rem;}

    /* Skills Columns */
    .skill-wrap{margin-bottom:20px;}
    .skill-name{font-size:0.85rem;}

    /* Info Cards */
    .info-card{padding:14px 16px;}
    .ic-title{font-size:0.95rem;}

    /* Contact Form */
    .c-form input,.c-form textarea{font-size:0.85rem!important;padding:10px 12px!important;}

    /* Hide decorative elements on mobile */
    .glow-orb-1,.glow-orb-2,.glow-orb-3{display:none;}

    /* Typewriter text fix */
    .typewriter-text{font-size:0.6rem;letter-spacing:3px;}
}

/* Large Phones (640px and below) */
@media(max-width:640px){
    .hero-name{font-size:2.4rem;}
    .hero-photo-wrap{max-width:240px;}
    .sec-title{font-size:1.8rem;}
    .about-text{font-size:0.9rem;line-height:1.8;}
    .trait-chip{font-size:0.6rem;padding:4px 12px;margin:3px;}
    .dl-btn{font-size:0.7rem;padding:10px 20px;}
    .proj-preview{height:160px;}
    .tech-badge{font-size:0.6rem;padding:2px 8px;}
}

/* Small Phones (480px and below) */
@media(max-width:480px){
    .hero-name{font-size:2rem;letter-spacing:0.5px;}
    .hero-role{font-size:0.7rem;letter-spacing:2px;}
    .hero-desc{font-size:0.85rem;line-height:1.7;}
    .hero-photo-wrap{max-width:200px;border-radius:12px;}
    .sec-title{font-size:1.6rem;}
    .sec-eyebrow{font-size:0.55rem;letter-spacing:3px;}
    .sec-eyebrow::before{width:20px;}

    /* KPI Cards - 2x2 Grid */
    .kpi-strip{flex-wrap:wrap;}
    .kpi-card{flex:0 1 calc(50% - 6px);min-width:auto;}
    .kpi-num{font-size:1.3rem;}

    /* Project Cards */
    .proj-card-body{padding:14px 16px 16px;}
    .proj-title{font-size:1rem;}
    .proj-desc{font-size:0.75rem;line-height:1.6;}
    .proj-link{font-size:0.65rem;padding:8px 16px;}

    /* Skills */
    .skill-group-title{font-size:0.65rem;}
    .skill-name{font-size:0.8rem;}
    .skill-pct{font-size:0.7rem;}

    /* Certs */
    .cert-card{padding:20px 18px;min-height:auto;}
    .cert-name{font-size:0.95rem;}

    /* Contact */
    .soc-btn{font-size:0.65rem;padding:8px 16px;}

    /* Footer */
    .footer{font-size:0.6rem;padding:24px 0 16px;}
}

/* Extra Small Phones (360px and below) */
@media(max-width:360px){
    .hero-name{font-size:1.7rem;}
    .hero-photo-wrap{max-width:180px;}
    .sec-title{font-size:1.4rem;}
    .learn-tag{font-size:0.55rem;padding:3px 10px;}
    .kpi-num{font-size:1.1rem;}
    .kpi-lbl{font-size:0.45rem;letter-spacing:1px;}
}

/* Landscape Mode Optimization */
@media(max-height:500px) and (orientation:landscape){
    .hero-wrap{padding-top:70px;padding-bottom:40px;}
    .hero-photo-wrap{max-width:180px;}
    .navbar{height:50px;}
}

/* High DPI / Retina Displays */
@media(-webkit-min-device-pixel-ratio:2),(min-resolution:192dpi){
    .hero-photo-wrap img{image-rendering:-webkit-optimize-contrast;}
}

/* Print Styles */
@media print{
    .navbar,.glow-orb,.glow-orb-1,.glow-orb-2,.glow-orb-3,#particle-canvas,#galaxy-overlay{display:none!important;}
    .hero-wrap{flex-direction:row;padding-top:20px;}
    .section{page-break-inside:avoid;}
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
html{overflow-y:scroll!important;scroll-behavior:smooth!important;scroll-padding-top:80px!important;}
body{overflow:visible!important;height:auto!important;}
section[data-testid="stMain"]{overflow-y:auto!important;height:100vh!important;scroll-behavior:smooth!important;scroll-padding-top:80px!important;}
section[data-testid="stMain"]::-webkit-scrollbar{width:5px!important;}
section[data-testid="stMain"]::-webkit-scrollbar-track{background:#0f0c06!important;}
section[data-testid="stMain"]::-webkit-scrollbar-thumb{background:#b8860b!important;border-radius:3px!important;}
.appview-container{overflow-y:auto!important;height:100vh!important;}
.appview-container::-webkit-scrollbar-thumb{background:#b8860b!important;border-radius:3px!important;}
[data-testid="block-container"],[data-testid="stVerticalBlock"]{overflow:visible!important;height:auto!important;max-height:none!important;}

/* Responsive Column Adjustments */
@media(max-width:768px){
    [data-testid="stHorizontalBlock"]{flex-direction:column!important;}
    [data-testid="column"]{width:100%!important;flex:1 1 100%!important;min-width:auto!important;padding-left:0!important;padding-right:0!important;margin-bottom:20px!important;}
}
</style>
<script>
(function fix(){
    var m=document.querySelector('section[data-testid="stMain"]');
    if(m){m.style.setProperty('overflow-y','auto','important');m.style.setProperty('height','100vh','important');return;}
    var a=document.querySelector('.appview-container');
    if(a){a.style.setProperty('overflow-y','auto','important');a.style.setProperty('height','100vh','important');return;}
    setTimeout(fix,100);
})();
</script>
""", unsafe_allow_html=True)

_bg_tag = ""
if bg_b64:
    _bg_tag = (
        "<style>"
        ".stApp {"
        "  background-image:"
        "    linear-gradient(rgba(5,4,12,0.80), rgba(5,4,12,0.80)),"
        "    url('data:image/jpeg;base64," + (bg_b64 or "") + "') !important;"
        "  background-size: cover !important;"
        "  background-position: center !important;"
        "  background-attachment: fixed !important;"
        "  background-repeat: no-repeat !important;"
        "}"
        "[data-testid='stAppViewContainer'], section[data-testid='stMain'],"
        "[data-testid='block-container'], .main {"
        "  background: transparent !important;"
        "}"
        "</style>"
    )

st.markdown(
    _bg_tag +
    '<div id="galaxy-overlay"></div>'
    '<canvas id="particle-canvas"></canvas>'
    '<div class="glow-orb glow-orb-1"></div>'
    '<div class="glow-orb glow-orb-2"></div>'
    '<div class="glow-orb glow-orb-3"></div>'
    """
<!-- Pure CSS checkbox hack — works inside Streamlit iframes, zero JS needed -->
<nav class="bot-nav" id="bot-nav">
    <a class="bot-nav-item" href="#hero" data-mob-link><span class="bot-nav-icon">🏠</span><span class="bot-nav-lbl">Home</span></a>
    <a class="bot-nav-item" href="#about" data-mob-link><span class="bot-nav-icon">👤</span><span class="bot-nav-lbl">About</span></a>
    <a class="bot-nav-item" href="#skills" data-mob-link><span class="bot-nav-icon">⚡</span><span class="bot-nav-lbl">Skills</span></a>
    <a class="bot-nav-item" href="#projects" data-mob-link><span class="bot-nav-icon">🚀</span><span class="bot-nav-lbl">Projects</span></a>
    <a class="bot-nav-item" href="#contact" data-mob-link><span class="bot-nav-icon">✉️</span><span class="bot-nav-lbl">Contact</span></a>
</nav>
<nav class="navbar" id="top-navbar">
    <a class="nav-brand" href="#hero-eyebrow">SRIRAM <span>SAI</span></a>
    <div class="nav-links">
        <a class="nav-link" href="#about">About</a>
        <a class="nav-link" href="#education">Education &amp; Experience</a>
        <a class="nav-link" href="#skills">Skills</a>
        <a class="nav-link" href="#certifications">Certifications</a>
        <a class="nav-link" href="#projects">Projects</a>
        <a class="nav-link" href="#contact">Contact</a>
    </div>
    <a class="nav-cta" href="mailto:sriramsailaggisetti@gmail.com">LET'S BUILD TOGETHER</a>

</nav>
<script>
(function(){
    var canvas=document.getElementById("particle-canvas");
    if(!canvas)return;
    var ctx=canvas.getContext("2d"),W,H,particles=[];
    function resize(){W=canvas.width=window.innerWidth;H=canvas.height=window.innerHeight;}
    resize();window.addEventListener("resize",resize);
    var C=["rgba(255,255,255,","rgba(255,255,255,","rgba(240,192,64,","rgba(212,160,23,","rgba(200,180,150,"];
    for(var i=0;i<180;i++){var big=Math.random()<0.05;particles.push({x:Math.random()*window.innerWidth,y:Math.random()*window.innerHeight,r:big?Math.random()*2.5+1:Math.random()*1.2+0.2,a:Math.random()*0.7+0.1,spd:Math.random()*0.12+0.02,drift:(Math.random()-0.5)*0.08,col:C[Math.floor(Math.random()*C.length)],tw:Math.random()*Math.PI*2,tws:Math.random()*0.025+0.003,shoot:false,stimer:Math.random()*400});}
    function shoot(p){p.stimer--;if(p.stimer<=0){p.shoot=true;p.stimer=Math.random()*600+200;p.sx=Math.random()*W;p.sy=Math.random()*H*0.5;p.sl=Math.random()*80+40;p.so=1;}if(p.shoot){ctx.beginPath();ctx.moveTo(p.sx,p.sy);ctx.lineTo(p.sx-p.sl,p.sy+p.sl*0.3);var g=ctx.createLinearGradient(p.sx,p.sy,p.sx-p.sl,p.sy+p.sl*0.3);g.addColorStop(0,"rgba(255,255,255,"+p.so+")");g.addColorStop(1,"rgba(255,255,255,0)");ctx.strokeStyle=g;ctx.lineWidth=1.5;ctx.stroke();p.so-=0.025;if(p.so<=0)p.shoot=false;}}
    function draw(){ctx.clearRect(0,0,W,H);particles.forEach(function(p){p.tw+=p.tws;var op=p.a*(0.3+0.7*Math.abs(Math.sin(p.tw)));ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle=p.col+op+")";ctx.fill();if(p.r>1.5){ctx.beginPath();ctx.arc(p.x,p.y,p.r*2.5,0,Math.PI*2);ctx.fillStyle=p.col+(op*0.15)+")";ctx.fill();}shoot(p);p.y-=p.spd;p.x+=p.drift;if(p.y<-5){p.y=H+5;p.x=Math.random()*W;}if(p.x<-5)p.x=W+5;if(p.x>W+5)p.x=-5;});requestAnimationFrame(draw);}
    draw();
})();
</script>
<script>
(function(){
    function init(){
        var links=document.querySelectorAll('[data-mob-link]');
        if(!links.length){setTimeout(init,200);return;}
        links.forEach(function(a){
            a.addEventListener('click',function(e){
                e.preventDefault();
                var href=this.getAttribute('href');
                var el=document.querySelector(href);
                if(el) el.scrollIntoView({behavior:'smooth',block:'start'});
                // highlight active
                links.forEach(function(l){l.classList.remove('active');});
                a.classList.add('active');
            });
        });
    }
    if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',init);}
    else{init();}
})();
</script>
""",
    unsafe_allow_html=True
)

if img_b64:
    photo_html = '<div class="hero-photo-wrap"><img src="data:image/png;base64,' + img_b64 + '" alt="Sriram Sai" /></div>'
else:
    photo_html = '<div class="hero-photo-wrap" style="height:460px;background:rgba(184,134,11,0.05);display:flex;align-items:center;justify-content:center;"><span style="font-size:5rem">👤</span></div>'

resume_btn = ""
try:
    with open("assets/SRIRAMSAI_RESUME.pdf", "rb") as f:
        rb64 = base64.b64encode(f.read()).decode()
    resume_btn = '<a class="dl-btn" href="data:application/pdf;base64,' + rb64 + '" download="SRIRAMSAI_Resume.pdf">⬇ DOWNLOAD RESUME</a>'
except:
    pass

st.markdown(
    '<div id="hero"><div class="section-hero"><div class="hero-wrap">'
    '<div class="hero-left">'
    '<div id ="hero-eyebrow" class="hero-eyebrow"><span class="typewriter-text">INITIALIZING </span></div>'
    '<div class="hero-name">SRIRAM SAI<br><span>LAGGISETTI</span></div>'
    '<div class="hero-role">AI &amp; ML Engineer &nbsp;·&nbsp; Data Scientist</div>'
    '<div class="hero-desc">Final-year B.Tech CSE student at Aditya Engineering College (Graduating 2026) — passionate about '
    '<strong style="color:#fdfcf7;">Data Science, AI &amp; ML</strong>, building intelligent systems that solve real problems. '
    'Actively seeking <strong style="color:#fdfcf7;">full-time roles</strong> in AI / ML / Data Science.</div>'
    '<div class="learn-strip"><span class="learn-lbl">NOW LEARNING</span>'
    '<span class="learn-tag">Docker</span><span class="learn-tag">AWS / Cloud</span><span class="learn-tag">FastAPI</span></div>'
    '<div class="kpi-strip">'
    '<div class="kpi-card"><div class="kpi-num">5+</div><div class="kpi-lbl">Projects</div></div>'
    '<div class="kpi-card"><div class="kpi-num">7.37</div><div class="kpi-lbl">CGPA</div></div>'
    '<div class="kpi-card"><div class="kpi-num">3</div><div class="kpi-lbl">Internships</div></div>'
    '<div class="kpi-card"><div class="kpi-num">4</div><div class="kpi-lbl">Certifications</div></div>'
    '</div>'
    '<div style="margin-top:8px;">' + resume_btn + '</div>'
    '</div>'
    '<div class="hero-right">' + photo_html + '</div>'
    '</div></div></div>',
    unsafe_allow_html=True
)
st.markdown('<div class="gold-div"></div>', unsafe_allow_html=True)


st.markdown("""
<div id="about" class="section">
    <div class="sec-eyebrow">WHO AM I</div>
    <div class="sec-title">About <span>Me</span></div>
    <div class="about-text">
        I'm <strong>Sriram Sai Laggisetti</strong> — a final-year B.Tech Computer Science student
        from Aditya Engineering College, Andhra Pradesh. I sit at the intersection of
        <strong>Artificial Intelligence, Machine Learning, and Data Science</strong>, turning complex
        problems into elegant, intelligent solutions.<br><br>
        My journey started with curiosity about how machines learn — and it quickly grew into a
        full-blown passion. I've built and deployed real-world AI applications: from
        <strong>LLM-powered chatbots</strong> and <strong>RAG pipelines</strong> to
        <strong>Stable Diffusion image generators</strong> and <strong>interactive analytics dashboards</strong>
        — all live on the web for anyone to use.<br><br>
        Beyond the code, I believe in <strong>clean design, fast iteration, and shipping things that matter</strong>.
        I don't just build models — I build products.
    </div>
    <div class="about-highlight">
        "Final-year student graduating April / May 2026 — actively seeking full-time roles in AI / ML / Data Science
        where I can contribute, grow, and keep building things that make a difference."
    </div>
    <div>
        <span class="trait-chip">⚡ ADAPTABILITY</span>
        <span class="trait-chip">🔁 CONSISTENCY</span>
        <span class="trait-chip">🤝 COLLABORATION</span>
        <span class="trait-chip">🧠 PROBLEM SOLVING</span>
        <span class="trait-chip">🚀 FAST LEARNER</span>
        <span class="trait-chip">🎨 DESIGN THINKING</span>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('<div class="gold-div"></div>', unsafe_allow_html=True)

col_e1, col_e2 = st.columns(2)
with col_e1:
    st.markdown("""
    <div id="education" class="section" style="padding-top:60px;padding-right:24px;">
        <div class="sec-eyebrow">ACADEMICS</div>
        <div class="sec-title">Edu<span>cation</span></div>
        <div class="info-card"><div class="ic-title">Aditya Engineering College</div><div class="ic-sub">B.Tech — Computer Science Engineering</div><div class="ic-detail">CGPA: 7.33 · 2022–2026 &nbsp;·&nbsp; 🎓 Graduating Apr / May 2026</div></div>
        <div class="info-card"><div class="ic-title">Sri Chaitanya Jr College</div><div class="ic-sub">MPC · Intermediate</div><div class="ic-detail">Grade: 77% · 2020–2022</div></div>
        <div class="info-card"><div class="ic-title">Sri Swamy Vivekananda School</div><div class="ic-sub">SSC · 10th Standard</div><div class="ic-detail">Grade: 95% · 2019–2020</div></div>
    </div>
    """, unsafe_allow_html=True)
with col_e2:
    st.markdown("""
    <div id="experience" class="section" style="padding-top:60px;padding-left:24px;">
        <div class="sec-eyebrow">WORK</div>
        <div class="sec-title">Experi<span>ence</span></div>
        <div class="info-card"><div class="ic-title">Infinitude Internship</div><div class="ic-sub">AI / ML Engineer Intern</div><div class="ic-detail">📍 Hyderabad · May – June 2025</div></div>
        <div class="info-card"><div class="ic-title">Cognifyz Internship</div><div class="ic-sub">Data Science Intern</div><div class="ic-detail">🌐 Online · June – July 2025</div></div>
        <div class="info-card"><div class="ic-title">SkillDzire Internship</div><div class="ic-sub">Python / ML Intern</div><div class="ic-detail">🌐 Online · July – Aug 2024</div></div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('<div class="gold-div"></div>', unsafe_allow_html=True)

# ── SKILLS ────────────────────────────────────────────────────────────────────
st.markdown('<div id="skills" class="section">', unsafe_allow_html=True)
st.markdown('<div class="sec-eyebrow">TECH STACK</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">My <span>Skills</span></div>', unsafe_allow_html=True)

def skill_bar(icon, name, pct):
    st.markdown(
        '<div class="skill-wrap"><div class="skill-row">'
        '<span class="skill-name"><span class="skill-icon">' + icon + '</span>' + name + '</span>'
        '<span class="skill-pct">' + str(pct) + '%</span></div>'
        '<div class="skill-track"><div class="skill-fill" style="width:' + str(pct) + '%"></div></div></div>',
        unsafe_allow_html=True
    )

sc1, sc2, sc3 = st.columns(3)
with sc1:
    st.markdown('<div class="skill-group-title">💻 TECHNICAL</div>', unsafe_allow_html=True)
    for icon,n,p in [("🐍","Python",88),("🤖","Machine Learning",80),("🧠","Deep Learning",65),("🦜","LLMs / LangChain",75)]:
        skill_bar(icon,n,p)
with sc2:
    st.markdown('<div class="skill-group-title">📊 DATA & TOOLS</div>', unsafe_allow_html=True)
    for icon,n,p in [("🔍","Data Analysis",82),("📊","Streamlit",85),("📈","Power BI / Plotly",72),("🗄️","SQL",70)]:
        skill_bar(icon,n,p)
with sc3:
    st.markdown('<div class="skill-group-title">🤝 SOFT SKILLS</div>', unsafe_allow_html=True)
    for icon,n,p in [("🗣️","Communication",85),("💡","Problem Solving",88),("🤝","Teamwork",83),("⚡","Adaptability",90)]:
        skill_bar(icon,n,p)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="gold-div"></div>', unsafe_allow_html=True)

st.markdown("""
<div id="certifications" class="section">
    <div class="sec-eyebrow">CREDENTIALS</div>
    <div class="sec-title">Certifi<span>cations</span></div>
    <div class="cert-grid">
        <div class="cert-card"><div class="cert-icon">🔷</div><div class="cert-name">OCI 2025 Generative AI Professional</div><div class="cert-issuer">Oracle</div><span class="cert-badge">✓ VERIFIED</span></div>
        <div class="cert-card"><div class="cert-icon">🤖</div><div class="cert-name">Gen AI: Prompt Engineering Basic</div><div class="cert-issuer">IBM</div><span class="cert-badge">✓ VERIFIED</span></div>
        <div class="cert-card"><div class="cert-icon">🐍</div><div class="cert-name">Python (Basic & Problem Solving)</div><div class="cert-issuer">HackerRank</div><span class="cert-badge">✓ VERIFIED</span></div>
        <div class="cert-card"><div class="cert-icon">🗄️</div><div class="cert-name">SQL (Basic & Intermediate)</div><div class="cert-issuer">HackerRank / Kaggle</div><span class="cert-badge">✓ VERIFIED</span></div>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('<div class="gold-div"></div>', unsafe_allow_html=True)

st.markdown('<div id="projects" class="section">', unsafe_allow_html=True)
st.markdown("<div class=\"sec-eyebrow\">WHAT I'VE BUILT</div>", unsafe_allow_html=True)
st.markdown('<div class="sec-title">My <span>Projects</span></div>', unsafe_allow_html=True)

projects = [
    {
        "num":"01","title":"🤖 AI TURBO CHAT — LLM CHATBOT",
        "desc":"Intelligent AI chatbot built with HuggingFace Transformers, LangChain & Streamlit. Powered by TinyLlama 1.1B for real-time, context-aware responses. Deployed live on HuggingFace Spaces with Docker.",
        "badges":["Python","LangChain","TinyLlama","Streamlit","HuggingFace","Docker"],
        "btn":"▶ LIVE DEMO","link":"https://huggingface.co/spaces/sriiram18/turbochat",
        "screenshot":"assets/proj01.png","placeholder_icon":"🤖",
    },
    {
        "num":"02","title":"📄 QUERYDOCS AI — PDF Q&A RAG PIPELINE",
        "desc":"Upload any PDF and ask questions in natural language! LangChain + FAISS + TinyLlama 1.1B. Full RAG pipeline — chunking, embedding, retrieval and context-aware answers.",
        "badges":["LangChain","FAISS","RAG","TinyLlama","HuggingFace","Docker"],
        "btn":"▶ LIVE DEMO","link":"https://huggingface.co/spaces/sriiram18/Querydocs",
        "screenshot":"assets/proj02.png","placeholder_icon":"📄",
    },
    {
        "num":"03","title":"📊 SALES & REVENUE INTELLIGENCE DASHBOARD",
        "desc":"Interactive dashboard with 5 live KPI cards, revenue trends, category bars, regional donuts, top-products rankings, profit margin analysis and 4 dynamic filters.",
        "badges":["Python","Streamlit","Plotly","Pandas","Data Visualization"],
        "btn":"📊 LIVE DASHBOARD","link":"https://salesdashboard18.streamlit.app/",
        "screenshot":"assets/proj03.png","placeholder_icon":"📊",
    },
    {
        "num":"04","title":"🏏 IPL DATA ANALYSIS — CRICKET INSIGHTS",
        "desc":"Comprehensive IPL analytics dashboard covering 14 seasons (2010–2023). 7 tabs — team win rates, top batsmen & bowlers, toss impact, venue stats, season trends and Player of Match awards.",
        "badges":["Python","Streamlit","Plotly","Pandas","EDA","Sports Analytics"],
        "btn":"📊 LIVE DASHBOARD","link":"https://dataanalysis18.streamlit.app/",
        "screenshot":"assets/proj04.png","placeholder_icon":"🏏",
    },
    {
        "num":"05","title":"🎨 AI IMAGE GENERATOR — STABLE DIFFUSION v1.5",
        "desc":"Text-to-image generation powered by RunwayML Stable Diffusion v1.5. Negative prompts, CFG scale, seed control. Generates stunning AI images from natural language descriptions.",
        "badges":["Python","Stable Diffusion v1.5","PyTorch","HuggingFace","Gradio","Diffusers"],
        "btn":"▶ LIVE DEMO","link":"https://huggingface.co/spaces/sriiram18/Ai-Image-Generator",
        "screenshot":"assets/proj05.png","placeholder_icon":"🎨",
    },
]

def _make_preview(p):
    if p.get("screenshot"):
        try:
            with open(p["screenshot"], "rb") as f:
                sdata = base64.b64encode(f.read()).decode()
            ext  = p["screenshot"].split(".")[-1].lower()
            mime = "image/jpeg" if ext in ("jpg","jpeg") else "image/png"
            return (
                '<div class="proj-preview">'
                '<img src="data:' + mime + ';base64,' + sdata + '" alt="' + p["title"] + '" />'
                '<div class="proj-preview-overlay"></div>'
                '</div>'
            )
        except:
            pass
    icon = p.get("placeholder_icon", "🚀")
    return (
        '<div class="proj-preview">'
        '<div class="proj-preview-placeholder">'
        '<div style="font-size:3.5rem">' + icon + '</div>'
        '<div style="font-family:\'Share Tech Mono\',monospace;font-size:0.6rem;'
        'color:rgba(184,134,11,0.5);letter-spacing:3px;margin-top:6px;">LIVE APP</div>'
        '</div>'
        '</div>'
    )

_cards_html = ""
for p in projects:
    _badges = "".join('<span class="tech-badge">' + b + '</span>' for b in p["badges"])
    _cards_html += (
        '<div class="proj-card">'
        + _make_preview(p) +
        '<div class="proj-card-body">'
        '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;">'
        '<div class="proj-num">PROJECT ' + p["num"] + '</div>'
        '<span class="feat-badge">✦ FEATURED</span>'
        '</div>'
        '<div class="proj-title">' + p["title"] + '</div>'
        '<div class="proj-desc">' + p["desc"] + '</div>'
        '<div style="margin-bottom:4px;">' + _badges + '</div>'
        '<a class="proj-link" href="' + p["link"] + '" target="_blank">' + p["btn"] + '</a>'
        '</div></div>'
    )

st.markdown('<div class="proj-grid">' + _cards_html + '</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="gold-div"></div>', unsafe_allow_html=True)

col_c1, col_c2 = st.columns((3, 2))
with col_c1:
    st.markdown("""
    <div id="contact" class="section" style="padding-right:24px;">
        <div class="sec-eyebrow">GET IN TOUCH</div>
        <div class="sec-title">Contact <span>Me</span></div>
        <form class="c-form" action="https://formsubmit.co/sriramsailaggisetti@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message" required></textarea>
            <button type="submit">▶ SEND MESSAGE</button>
        </form>
    </div>
    """, unsafe_allow_html=True)
with col_c2:
    st.markdown("""
    <div class="section" style="padding-top:80px;padding-left:24px;">
        <div class="sec-eyebrow">CONNECT</div>
        <div class="sec-title" style="font-size:1.8rem;">Find Me<br><span>Online</span></div>
        <div style="display:flex;flex-direction:column;gap:0;">
            <a class="soc-btn" href="https://www.linkedin.com/in/sriram-sai-laggisetti/" target="_blank">💼 &nbsp; LinkedIn</a>
            <a class="soc-btn" href="https://github.com/sriramsai18" target="_blank">💻 &nbsp; GitHub</a>
            <a class="soc-btn" href="https://www.instagram.com/sriiram.18/" target="_blank">📸 &nbsp; Instagram</a>
            <a class="soc-btn" href="mailto:sriramsailaggisetti@gmail.com">✉️ &nbsp; Email Me</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    CRAFTED BY ✦
    <a href="https://github.com/sriramsai18" target="_blank">SRIRAM SAI LAGGISETTI</a>
    &nbsp;·&nbsp; @2026
</div>
""", unsafe_allow_html=True)
