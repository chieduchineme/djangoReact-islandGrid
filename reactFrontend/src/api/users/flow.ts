import axios from 'axios';
import { FlowResult } from '../../types/types';

/**
 * Fetches data for a specific case from the API.
 * 
 * This function makes an HTTP GET request to the API endpoint for a given case ID.
 * It returns a promise that resolves with the case data in the form of a `FlowResult` object.
 * 
 * @param caseId - The ID of the case to fetch data for.
 * @returns A promise that resolves with the data of type `FlowResult` corresponding to the requested case.
 * 
 * @throws Will throw an error if the request fails.
 * 
 * @example
 */
export const fetchCaseData = async (caseId: number): Promise<FlowResult> => {
  const response = await axios.get<FlowResult>(`http://127.0.0.1:8000/api/case/${caseId}/`);
  console.log(response);
  return response.data;
};
