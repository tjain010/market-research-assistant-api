import { useState } from "react";
import "./App.css";

function App() {
  const [topic, setTopic] = useState("");
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError("");
    setReport(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/plan", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ topic }),
      });

      if (!response.ok) {
        throw new Error("Failed to generate report");
      }

      const data = await response.json();
      setReport(data);
    } catch (err) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>Market Research Assistant</h1>
      <p className="subtitle">
        Enter a topic to generate a structured research plan.
      </p>

      <form onSubmit={handleSubmit} className="topic-form">
        <input
          type="text"
          placeholder="Try: IBM AI strategy"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          className="topic-input"
        />
        <button type="submit" className="submit-button" disabled={loading}>
          {loading ? "Generating..." : "Generate Report"}
        </button>
      </form>

      {error && <p className="error-text">{error}</p>}

      {report && (
        <div className="report-card">
          <h2>Research Plan</h2>
          <p><strong>Report ID:</strong> {report.report_id}</p>
          <p><strong>Topic:</strong> {report.topic}</p>
          <p><strong>Research Type:</strong> {report.research_type}</p>
          <p><strong>Next Step:</strong> {report.next_step}</p>

          <section>
            <h3>Subquestions</h3>
            <ul>
              {report.subquestions.map((question, index) => (
                <li key={index}>{question}</li>
              ))}
            </ul>
          </section>

          <section>
            <h3>Report Outline</h3>
            <ul>
              {report.report_outline.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          </section>

          <section>
            <h3>Keywords</h3>
            <ul>
              {report.keywords.map((keyword, index) => (
                <li key={index}>{keyword}</li>
              ))}
            </ul>
          </section>

          <section>
            <h3>Suggested Sources</h3>
            <ul>
              {report.suggested_sources.map((source, index) => (
                <li key={index}>{source}</li>
              ))}
            </ul>
          </section>

          <section>
            <h3>Starter Sources</h3>
            <ul>
              {report.starter_sources.map((source, index) => (
                <li key={index}>
                  <a href={source.url} target="_blank" rel="noreferrer">
                    {source.label}
                  </a>
                </li>
              ))}
            </ul>
          </section>
        </div>
      )}
    </div>
  );
}

export default App;