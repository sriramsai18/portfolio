import { Link } from "react-router-dom";
import Topbar from "../components/Topbar";
import { DATA } from "../data";

const CERT_PREVIEW = 3;

export default function Home() {
  return (
    <div className="page">
      <Topbar />

      {/* ── Hero ── */}
      <h1 className="hero-name">{DATA.name}.</h1>
      <p className="hero-sub">{DATA.tagline}</p>

      <div className="hero-bio-row">
        <img
          className="hero-photo"
          src="/NANII.png"
          alt={DATA.name}
          onError={e => { e.target.style.display = "none"; }}
        />
        <p className="hero-bio-text">{DATA.bio}</p>
      </div>

      {/* ── Experience ── */}
      <section className="section">
        <div className="section-header">
          <span className="section-label">experience</span>
          <span className="section-rule" />
          <span className="section-count">{DATA.experience.length} entries</span>
        </div>
        {DATA.experience.map((e, i) => (
          <div className="entry experience-entry" key={i}>
            <span className="entry-star">✦</span>
            <span className="entry-main entry-main-blue">
              {e.role}
              <span className="entry-meta"> @ {e.org} &nbsp;[{e.period}]</span>
            </span>
          </div>
        ))}
      </section>

      {/* ── Projects ── */}
      <section className="section">
        <div className="section-header">
          <span className="section-label">projects</span>
          <span className="section-rule" />
          <span className="section-count">{DATA.projects.length} entries</span>
        </div>
        {DATA.projects.map((p, i) => (
          <div className="entry" key={i}>
            <span className="entry-star">✦</span>
            <span className="entry-main">
              <a href={p.href} target="_blank" rel="noreferrer">{p.label}</a>
              <span className="entry-tag">{p.role}</span>
              <span className="entry-meta"> — {p.desc}</span>
            </span>
          </div>
        ))}
        <Link to="/projects" className="more-link">
          view all projects &rarr;
        </Link>
      </section>

      {/* ── Certifications (preview 3) ── */}
      <section className="section">
        <div className="section-header">
          <span className="section-label">certifications</span>
          <span className="section-rule" />
          <span className="section-count">{DATA.certifications.length} entries</span>
        </div>
        {DATA.certifications.slice(0, CERT_PREVIEW).map((c, i) => (
          <div className="entry" key={i}>
            <span className="entry-star">✦</span>
            <span className="entry-main">
              <a href={c.href} target="_blank" rel="noreferrer">{c.label}</a>
              <span className="entry-meta"> — {c.desc}</span>
            </span>
          </div>
        ))}
      </section>

      {/* ── Education ── */}
      <section className="section">
        <div className="section-header">
          <span className="section-label">education</span>
          <span className="section-rule" />
        </div>
        {DATA.education.map((e, i) => (
          <div className="entry" key={i}>
            <span className="entry-star">✦</span>
            <span className="entry-main">
              {e.internal
                ? <Link to={e.route}>{e.label}</Link>
                : <a href={e.href} target="_blank" rel="noreferrer">{e.label}</a>
              }
              <span className="entry-meta"> — {e.desc}</span>
            </span>
          </div>
        ))}
      </section>

      {/* ── Pages ── */}
      <section className="section">
        <div className="section-header">
          <span className="section-label">pages</span>
          <span className="section-rule" />
        </div>
        {DATA.pages.map((p, i) => (
          <div className="entry" key={i}>
            <span className="entry-star">✦</span>
            <span className="entry-main">
              <a href={p.href} target="_blank" rel="noreferrer">{p.label}</a>
            </span>
          </div>
        ))}
      </section>

      {/* ── Footer ── */}
      <footer className="site-footer">
        <div className="footer-links">
          <a href={DATA.email}>connect</a>
          <a href={DATA.github} target="_blank" rel="noreferrer">github</a>
          <a href={DATA.linkedin} target="_blank" rel="noreferrer">linkedin</a>
          <a href={DATA.huggingface} target="_blank" rel="noreferrer">hf.co</a>
        </div>
        <span>last updated: may 2026'</span>
      </footer>
    </div>
  );
}
