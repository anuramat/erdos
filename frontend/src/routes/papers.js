import 'papers.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';

export const Papers = () => {
    const nav = useNavigate();
    const navToRegister = () => nav('/registration');

    return (
        <div className="background p-5">
            <div class="row">
                <div class="col-3 left-menu">
                    <input type="email" class="form" id="email" placeholder="email" />
                    <input type="password" class="form" id="password" placeholder="password" />
                    <button className="button"> Log in </button>
                    <button className="button" onClick={navToRegister}>Register</button>
                </div>
                <div className="col ms-5">
                    <div className="content-container">
                        <input type="text" class="search-form" id="search" placeholder="Paper search" />
                    </div>
                    <div className="content-container mt-5">
                        tabs : (latest papers / search query / recommendations)
                        <br />
                        if search : (results for searchterm: )
                    </div>
                </div>
            </div>

        </div>
    );
}

