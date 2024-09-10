import App from '@/App';
import { createBrowserRouter, createRoutesFromElements, Route } from 'react-router-dom';

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route
      path=''
      element={<App />}>
    </Route>
  )
);

export default router;
