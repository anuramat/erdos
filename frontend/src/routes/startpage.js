import logo from 'logo.svg';
import 'App.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';

export const StartPage = () => {
    return (
        <div className="background">
            <div className="middle-column">
                <img src={logo} alt="logo" />
                <div className="index-message"> Welcome! </div>
                <button className="button">Log in</button>
                <button className="button">Sign up</button>
                <button className="button">Guest mode</button>
            </div>
        </div>
    );
}