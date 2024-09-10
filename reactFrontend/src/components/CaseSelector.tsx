// src/components/CaseSelector.tsx
import React from 'react';
import styles from '../styles/CaseSelector.module.css';  // Importing the styles
import { CaseSelectorProps } from '../types/types';

/**
 * A component for selecting a case number from a dropdown.
 * 
 * @param {number} selectedCase - The currently selected case number.
 * @param {Function} onCaseChange - A callback function to handle changes in the selected case.
 * 
 * @returns {JSX.Element} The rendered CaseSelector component.
 * 
 * @example
 * <CaseSelector
 *   selectedCase={2}
 *   onCaseChange={(newCase) => console.log(newCase)}
 * />
 */
const CaseSelector: React.FC<CaseSelectorProps> = ({ selectedCase, onCaseChange }) => {
  return (
    <div className={styles.container}>
      <label htmlFor="caseSelector" className={styles.label}>Select a Case: </label>
      <select 
        id="caseSelector"
        className={styles.select}
        value={selectedCase}
        onChange={(e) => onCaseChange(Number(e.target.value))}
      >
        {[1, 2, 3, 4, 5, 6].map((caseNumber) => (
          <option key={caseNumber} value={caseNumber}>
            Case {caseNumber}
          </option>
        ))}
      </select>
    </div>
  );
};

export default CaseSelector;
