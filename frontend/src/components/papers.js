import 'papers.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';


export const Tabs = {
    recent: "recent",
    recommended: "recommended",
    search: "search"
}

// tab, query, content
export const Papers = (props) => {
    const nav = useNavigate();
    const navToRegister = () => nav('/registration');
    const searchHandler = (e) => {
        if (e.key === "Enter") {
            let params = new URLSearchParams({ "q": e.target.value })
            nav('/search?' + params)
        }
    }

    const [formValues, setFormValues] = useState({});


    const formChange = (e) => {
        const { name, value } = e.target;
        setFormValues({ ...setFormValues, [name]: value });
    }

    return (
        <div className="background p-5">
            <div className="row">

                <div className="col-3">
                    <div className="left-menu">
                        <input type="text" className="form" placeholder="Paper search" onKeyPress={searchHandler} defaultValue={props.query} />
                    </div>

                    <div className="left-menu mt-5">
                        <input type="email" className="form" name="email" placeholder="email" onChange={formChange} />
                        <input type="password" className="form" name="password" placeholder="password" onChange={formChange} />
                        <button className="button"> Log in </button>
                        <button className="button" onClick={navToRegister}>Register</button>

                    </div>

                </div>
                <div className="col ms-5">

                    <div className="content-container">
                        <ul className="nav nav-pills nav-justified">
                            <li className="nav-item">
                                <a className={"nav-link" + (props.tab === Tabs.recommended ? " active" : "")} aria-current="page" href="/recommended">Recommended</a>
                            </li>
                            <li className="nav-item">
                                <a className={"nav-link" + (props.tab === Tabs.recent ? " active" : "")} aria-current="page" href="/recent">Recent</a>
                            </li>
                        </ul>

                        {props.content}

                    </div>
                </div>
            </div>

        </div >
    );
}

