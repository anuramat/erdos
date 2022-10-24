import { getUserData, isAuthenticated, logOut, setJWT } from 'auth';
import { useNavigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import 'papers.scss';
import { useState } from 'react';

export const Menu = (props) => {
    const nav = useNavigate();
    const navToRegister = () => nav('/registration');
    const logOutHandler = () => {
        logOut();
        nav('/');
    }

    const [loginError, setLoginError] = useState();

    const { register, handleSubmit } = useForm();

    const loginResponseHandler = (e) => {
        switch (e.status) {
            case 401:
            case 403:
            case 422:
                setLoginError("Wrong credentials, try again.");
                break;
            case 200:
                e.json().then(jwt => setJWT(jwt)).then(() => nav('/'))
                break;
            default:
                e.json().then((x) => setLoginError(x));
        }
    }

    const loginSubmitHandler = (e) => {
        // TODO fix backend addressing
        const backend_address = window.location.protocol + "//" + window.location.hostname + ":8080/";
        fetch(backend_address + 'login', {
            method: "POST", body: JSON.stringify(e), headers: {
                'Content-Type': 'application/json'
            }
        }).then(e => loginResponseHandler(e))
    }

    if (!isAuthenticated())
        return (
            <form className="left-menu" onSubmit={handleSubmit(loginSubmitHandler)}>
                <input type="email" className="form" placeholder="email" {...register("email")} />
                <input type="password" className="form" placeholder="password" {...register("password")} />
                <button className="button"> Log in </button>
                <button className="button" onClick={navToRegister}>Register</button>
                {loginError}

            </form>)
    else {
        return (
            <div className="left-menu">
                <div className="mb-3">
                    {getUserData().email}
                </div>

                <button className="button" onClick={logOutHandler}> Log out </button>
            </div>
        )
    }
}