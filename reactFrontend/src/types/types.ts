// src/types/types.ts

export interface FlowResult {
    case: string;
    qualifying_cells: number;
    coordinates: number[][];
  }
  
  export interface CaseSelectorProps {
    selectedCase: number;
    onCaseChange: (newCase: number) => void;
  }
  
  export interface ResultDisplayProps {
    qualifyingCells: number | null;
    coordinates: number[][];
    error: string | null;
  }
  