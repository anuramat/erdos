import logo from 'logo.svg';
import 'App.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';

export const Registration = () => {
    return (
        <div className="background">
            <div className="middle-column">
                <div className="index-message"> Registration </div>
                <input type="email" class="form" id="email" placeholder="email" />
                <input type="password" class="form" id="password" placeholder="password" />
                <input type="password" class="form" id="password_repeated" placeholder="password again" />
                <button className="button"> Sign up </button>
            </div>
        </div>)
}
