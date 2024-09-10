// src/App.tsx

import React, { useState, useEffect } from 'react';
import CaseSelector from './components/CaseSelector';
import ResultDisplay from './components/ResultDIsplay'; 
import { fetchCaseData } from './api/users/flow';
import { FlowResult } from './types/types';

/**
 * The App component is the main component of the application.
 * It is responsible for managing the state related to the selected case
 * and the results fetched from the server. It displays the CaseSelector
 * component for selecting different cases and the ResultDisplay component
 * to show the fetched results.
 * 
 * State Management:
 * - `selectedCase`: Stores the currently selected case number.
 * - `qualifyingCells`: Stores the number of qualifying cells for the selected case.
 * - `coordinates`: Stores the coordinates of the qualifying cells.
 * - `error`: Stores any error message that may occur during data fetching.
 * 
 * Effects:
 * - When `selectedCase` changes, it triggers a data fetch to retrieve
 *   results for the selected case and updates the state accordingly.
 * 
 * Components:
 * - `CaseSelector`: Allows the user to select a case number from a dropdown.
 * - `ResultDisplay`: Displays the results including qualifying cells count,
 *   coordinates, and any error messages.
 * 
 * @returns {React.FC} The App component
 */
const App: React.FC = () => {
  const [selectedCase, setSelectedCase] = useState<number>(1);
  const [qualifyingCells, setQualifyingCells] = useState<number | null>(null);
  const [coordinates, setCoordinates] = useState<number[][]>([]);
  const [error, setError] = useState<string | null>(null);

  // Fetch data when the selected case changes
  useEffect(() => {
    const fetchData = async () => {
      try {
        const data: FlowResult = await fetchCaseData(selectedCase);
        setQualifyingCells(data.qualifying_cells);
        setCoordinates(data.coordinates);
        setError(null);
      } catch (err) {
        setError('Failed to fetch data from the server.');
        setQualifyingCells(null);
        setCoordinates([]);
      }
    };

    fetchData();
  }, [selectedCase]);

  return (
    <div className="App">
      <h1>Water Flow Scenario Analysis</h1>
      
      <CaseSelector selectedCase={selectedCase} onCaseChange={setSelectedCase} />
      
      <ResultDisplay 
        qualifyingCells={qualifyingCells} 
        coordinates={coordinates} 
        error={error} 
      />
    </div>
  );
};

export default App;
