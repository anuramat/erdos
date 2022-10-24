import 'registration.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';

const States = {
    start: "",
    success: "Registered successfully",
}

const RegistrationForm = (props) => {

    const { register, handleSubmit } = useForm();
    const registrationResponseHandler = (e) => {
        switch (e.status) {
            case 200:
                props.setState(States.success);
                break;
            case 422:
                props.setState("Invalid credentials");
                break;
            default:
                e.json().then((x) => props.setState(x.detail));
        }
    }
    const formHandler = (e) => {
        if (e.password !== e.password_again) {
            props.setState("Passwords don't match")
            return
        }

        // TODO proper address
        const params = { email: e.email, password: e.password }
        const backend_address = window.location.protocol + "//" + window.location.hostname + ":8080/";
        fetch(backend_address + 'register', {
            method: "POST", body: JSON.stringify(params), headers: {
                'Content-Type': 'application/json'
            }
        }).then(e => registrationResponseHandler(e))
    }

    return (
        <form className="middle-column" onSubmit={handleSubmit(formHandler)}>
            <div > xd xd xd </div>
            <input type="email" className="form" placeholder="email" {...register("email")} />
            <input type="password" className="form" placeholder="password" {...register("password")} />
            <input type="password" className="form" placeholder="password again" {...register("password_again")} />
            < button type="submit" className="button">Register</button>
        </form >)
}

const FailedMessage = (props) => {
    return (
        <div className="middle-column mt-5">
            {props.children}
        </div>
    )

}

const SuccessMessage = (props) => {
    const nav = useNavigate();
    return (
        <div className="middle-column">
            {props.children}
            <button className="button" onClick={() => nav("/")}>Back to start page</button>
        </div>
    )
}

export const Registration = () => {
    const [state, setState] = useState(States.start);

    return (
        <div className="background p-5">
            {state !== States.success && <RegistrationForm setState={setState} />}
            {state === States.success && <SuccessMessage>{state}!</SuccessMessage>}
            {state !== States.success && state !== States.start && <FailedMessage>{state}</FailedMessage>}
        </div>)
}
