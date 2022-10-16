import logo from 'logo.svg';
import 'App.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate, BrowserRouter } from 'react-router-dom';
import { Router } from 'router';

export const App = () => {
  return (
    <BrowserRouter>
      {Router()}
    </BrowserRouter>
  )
}