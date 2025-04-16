import React from 'react'

function ColumnSelector({ selectedColumns, setSelectedColumns }) {
 const availableColumns = ['id', 'price', 'date', 'postcode', 'property_type'];  

 const toggleColumn = (column) => {
   if(selectedColumns.includes(column)){
    setSelectedColumns(selectedColumns.filter(c => c !== column));
   } else {
    setSelectedColumns([...selectedColumns, column]);
   }
 };

  return (
    <div style={{ marginTop: 20 }}>
      <h4>Select Columns:</h4>
      {availableColumns.map(col => (
        <label key={col} style={{ marginRight: 10 }}>
          <input
            type="checkbox"
            checked={selectedColumns.includes(col)}
            onChange={() => toggleColumn(col)}
          />
          {col}
        </label>
      ))}
    </div>
  );
}

export default ColumnSelector;
