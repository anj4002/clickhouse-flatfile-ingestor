import React from 'react';

function IngestPanel({ handleIngest, response }) {
  return (
    <div style={{ marginTop: 20 }}>
      <button onClick={handleIngest}>Start Ingestion</button>
      {response && (
        <div style={{ marginTop: 10 }}>
          {response.status === "success" ? (
            <p> Records Processed: {response.records}</p>
          ) : (
            <p> Error: {response.message}</p>
          )}
        </div>
      )}
    </div>
  );
}

export default IngestPanel;
