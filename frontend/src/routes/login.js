import logo from 'logo.svg';
import 'App.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';

export const Login = () => {
    return (
        <div className="background">
            <div className="middle-column">
                <div className="index-message"> Sign in </div>
                <input type="email" class="form" id="email" placeholder="email" />
                <input type="password" class="form" id="password" placeholder="password" />
                <button className="button"> Log in </button>
            </div>
        </div>)
}
