import { useEffect, useState } from "react";

export default function Home() {
  const [stocks, setStocks] = useState([]);

  useEffect(() => {
    const ws = new WebSocket("wss://YOUR-AZURE-URL/ws");

    ws.onmessage = (event) => {
      setStocks(JSON.parse(event.data));
    };

    return () => ws.close();
  }, []);

  return (
    <div style={{ background: "black", color: "white", padding: 20 }}>
      <h1>Equity Intelligence Dashboard</h1>

      {stocks.map((s, i) => (
        <div key={i} style={{
          display: "flex",
          justifyContent: "space-between",
          borderBottom: "1px solid gray",
          padding: "8px"
        }}>
          <span>{s.ticker}</span>
          <span>{s.score}</span>
          <span>{s.recommendation}</span>
        </div>
      ))}
    </div>
  );
}
