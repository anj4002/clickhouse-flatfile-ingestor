import React from 'react';

function SourceConfig({ source, target, clickhouseConfig, setClickhouseConfig, flatfileConfig, setFlatfileConfig, setTableName }) {
  return (
    <div style={{ marginTop: 10 }}>
      {/* Show these if ClickHouse is source */}
      {source === "ClickHouse" && (
        <>
        <input placeholder="Host" onChange={e => setClickhouseConfig({ ...clickhouseConfig, host: e.target.value })} />
        <input placeholder="Port" type="number" onChange={e => setClickhouseConfig({ ...clickhouseConfig, port: Number(e.target.value) })}/>
        <input placeholder="Database" onChange={e => setClickhouseConfig({ ...clickhouseConfig, database: e.target.value })} />
        <input placeholder="User" onChange={e => setClickhouseConfig({ ...clickhouseConfig, user: e.target.value })} />
        <input placeholder="JWT Token" onChange={e => setClickhouseConfig({ ...clickhouseConfig, jwt_token: e.target.value })} />
        <input placeholder="Table Name (e.g. uk_price_paid)" onChange={e => setTableName(e.target.value)} />
      </>
      )}

{target === "FlatFile" && (
        <>
          <input placeholder="File Path (e.g. C:/clickhouse-flatfile-ingestor/test.csv)" onChange={e => setFlatfileConfig({ ...flatfileConfig, filepath: e.target.value })} />
          <input placeholder="Delimiter (e.g. ,)" onChange={e => setFlatfileConfig({ ...flatfileConfig, delimiter: e.target.value })} />
        </>
      )}

{/* Show flat file config when it's the source */}
{source === "FlatFile" && (
        <>
          <input
            placeholder="File Path (e.g. C:/path/file.csv)"
            onChange={e => setFlatfileConfig({ ...flatfileConfig, filepath: e.target.value })}
          />
          <input
            placeholder="Delimiter (e.g. ,)"
            defaultValue=","
            onChange={e => setFlatfileConfig({ ...flatfileConfig, delimiter: e.target.value })}
          />
        </>
      )}

      {/* Show ClickHouse config when it's the target */}
      {target === "ClickHouse" && (
        <>
          <input
            placeholder="ClickHouse Host"
            onChange={e => setClickhouseConfig({ ...clickhouseConfig, host: e.target.value })}
          />
          <input
            placeholder="Port"
            onChange={e => setClickhouseConfig({ ...clickhouseConfig, port: e.target.value })}
          />
          <input
            placeholder="Database"
            onChange={e => setClickhouseConfig({ ...clickhouseConfig, database: e.target.value })}
          />
          <input
            placeholder="User"
            onChange={e => setClickhouseConfig({ ...clickhouseConfig, user: e.target.value })}
          />
          <input
            placeholder="JWT Token or Password"
            onChange={e => setClickhouseConfig({ ...clickhouseConfig, jwt_token: e.target.value })}
          />
          <input
            placeholder="Target Table Name (e.g. imported_table)"
            onChange={e => setTableName(e.target.value)}
          />
        </>
      )}

    </div>
  );
}

export default SourceConfig;
