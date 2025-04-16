import React, { useState } from 'react';
import axios from 'axios';
import SourceConfig from './components/SourceConfig';
import ColumnSelector from './components/ColumnSelector';
import IngestPanel from './components/IngestPanel';

function App() {
  const [source, setSource] = useState("ClickHouse");
  const [target, setTarget] = useState("FlatFile");

  const [clickhouseConfig, setClickhouseConfig] = useState({
    host: '', port: '', database: '', user: '', jwt_token: ''
  });

  const [flatfileConfig, setFlatfileConfig] = useState({
    filepath: '', delimiter: ','
  });

  const [tableName, setTableName] = useState('');
  const [selectedColumns, setSelectedColumns] = useState([
    'id', 'price', 'date', 'postcode', 'property_type'
  ]);

  const [response, setResponse] = useState(null);

  const handleIngest = async () => {
    const payload = {
      source,
      target,
      clickhouse_config: (source === "ClickHouse" || target === "ClickHouse") ? clickhouseConfig : null,
      flatfile_config: (source === "FlatFile" || target === "FlatFile") ? flatfileConfig : null,
      selected_columns: selectedColumns,
      table: tableName
    };

    try {
      const res = await axios.post("http://127.0.0.1:8000/ingest", payload);
      setResponse(res.data);
    } catch (err) {
      console.error("AxiosError:", err);
      setResponse({ status: 'error', message: err.message });
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Data Ingestion Tool</h2>
      <div>
        <label>Source:</label>
        <select value={source} onChange={e => setSource(e.target.value)}>
          <option value="ClickHouse">ClickHouse</option>
          <option value="FlatFile">FlatFile</option>
        </select>

        <label style={{ marginLeft: 10 }}>Target:</label>
        <select value={target} onChange={e => setTarget(e.target.value)}>
          <option value="FlatFile">FlatFile</option>
          <option value="ClickHouse">ClickHouse</option>
        </select>
      </div>

      <SourceConfig source={source} target={target}
        clickhouseConfig={clickhouseConfig} setClickhouseConfig={setClickhouseConfig}
        flatfileConfig={flatfileConfig} setFlatfileConfig={setFlatfileConfig}
        setTableName={setTableName} />

      <ColumnSelector selectedColumns={selectedColumns} setSelectedColumns={setSelectedColumns} />
      <IngestPanel handleIngest={handleIngest} response={response} />
    </div>
  );
}

export default App;