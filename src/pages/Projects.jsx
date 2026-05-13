import { Link } from "react-router-dom";
import Topbar from "../components/Topbar";
import { DATA } from "../data";

const PROJECTS = [
  
  {
    title: "clearwave ai",
    desc: "Audio enhancement web app for denoising, transcription, and translation using AI.",
    tags: ["audio-enhancement", "denoising", "transcription", "translation"],
    date: "completed: march 2026'",
    href: "https://clearwaveai.in",
  },
  {
    title: "Portfolio Website",
    desc: "A personal portfolio website built with React and Vite, showcasing projects and skills.",
    tags: ["react", "vite", "javascript"],
    date: "completed: april 2026'",
    href: "https://github.com/sriramsai18/portfolio",
  },
  {
    title: "Livnest Interiors Website",
    desc: "A website for Livnest Interiors, showcasing their interior design services and portfolio.",
    tags: ["html", "css", "javascript"],
    date: "ongoing",
    href: "null",
  },
  {
    title: "Employee Performance Prediction",
    desc: "Machine learning model for predicting employee performance based on various factors.",
    tags: ["python", "machine-learning", "data-analysis"],
    date: "completed: march 2026'",
    href: "https://github.com/sriramsai18/Employee_performance_prediction",
  },
  {
    title: "Sales & Revenue Dashboard",
    desc: "A responsive sales and revenue dashboard using Streamlit and Plotly</Plotly>.",
    tags: ["streamlit", "plotly", "data-visualization"],
    date: "completed: february 2026'",
    href: "https://salesdashboard18.streamlit.app/",
  },
  {
    title: "Amazon Sales Analysis",
    desc: "Analysis of Amazon sales data to identify patterns and trends.",
    tags: ["dashboard", "kpi's", "data-analysis"],
    date: "completed: january 2024'",
    href: "https://amazon18.streamlit.app/",
  },
  {
    title: "AI Image Generator",
    desc: "A web app for generating images from text prompts using Hugging Face's Stable Diffusion model.",
    tags: ["huggingface", "stable-diffusion", "text-to-image"],
    date: "completed: december 2025'",
    href: "https://huggingface.co/spaces/sriiram18/Ai-Image-Generator",
  },
  {
    title: "QueryDocs Ai",
    desc: "A document query tool that uses AI to answer questions based on uploaded documents.",
    tags: ["ai", "document-query", "question-answering"],
    date: "completed: november 2025'",
    href: "https://huggingface.co/spaces/sriiram18/Querydocs",
  },
  
];

export default function Projects() {
  return (
    <div className="page">
      <Topbar />
      <Link to="/" className="back-link">← back</Link>

      <h1 className="sub-title">projects</h1>
      <p className="sub-subtitle">
        8 entries &nbsp;·&nbsp; personal and professional projects
      </p>

      <section className="section">
        <div className="section-header">
          <span className="section-label">projects</span>
          <span className="section-rule" />
          <span className="section-count">8 projects</span>
        </div>
        <div className="doc-grid">
          {PROJECTS.map((project, i) => (
            <a
              key={i}
              href={project.href}
              target="_blank"
              rel="noreferrer"
              className="doc-card"
            >
              <div className="doc-card-title">{project.title}</div>
              <div className="doc-card-desc">{project.desc}</div>
              <div className="doc-card-tags">
                {project.tags.map((t, j) => (
                  <span key={j} className="entry-tag">{t}</span>
                ))}
              </div>
              <div className="doc-card-date">{project.date}</div>
            </a>
          ))}
        </div>
      </section>

      <footer className="site-footer">
        <div className="footer-links">
          <a href={DATA.email}>collaborate</a>
          <a href={DATA.linkedin} target="_blank" rel="noreferrer">linkedin</a>
        </div>
        <span>last updated: apr 2026'</span>
      </footer>
    </div>
  );
}
