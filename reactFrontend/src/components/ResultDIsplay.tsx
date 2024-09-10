// src/components/ResultDisplay.tsx
import React from 'react';
import styles from '../styles/ResultDisplay.module.css';  // Importing the styles
import { ResultDisplayProps } from '../types/types';

/**
 * ResultDisplay Component
 * 
 * Displays the results including the number of qualifying cells and their coordinates.
 * It also shows an error message if there is any error.
 * 
 * Props:
 * - qualifyingCells (number | null): The number of cells that meet the criteria. Displays 'Loading...' if null.
 * - coordinates (Array<[number, number]>): An array of coordinates where each coordinate is a tuple of [x, y].
 * - error (string | null): An error message to display. If null, no error message is shown.
 * 
 * @param {ResultDisplayProps} props - The component props.
 * @returns {JSX.Element} The rendered ResultDisplay component.
 */
const ResultDisplay: React.FC<ResultDisplayProps> = ({ qualifyingCells, coordinates, error }) => {
  if (error) {
    return <p className={styles.error}>{error}</p>;
  }

  return (
    <div className={styles.container}>
      <h2 className={styles.header}>Results</h2>
      <p>Number of qualifying cells: {qualifyingCells !== null ? qualifyingCells : 'Loading...'}</p>
      <h3 className={styles.subheader}>Qualifying Coordinates:</h3>
      <ul className={styles.list}>
        {coordinates.map((coord, index) => (
          <li key={index}>({coord[0]}, {coord[1]})</li>
        ))}
      </ul>
    </div>
  );
};

export default ResultDisplay;
