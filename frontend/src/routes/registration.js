import 'registration.scss';
import 'bootstrap/dist/css/bootstrap.min.css';

export const Registration = () => {
    return (
        <div className="background p-5">
            <div className="middle-column">
                <div className="index-message"> xd xd xd </div>
                <input type="email" className="form" id="email" placeholder="email" />
                <input type="password" className="form" id="password" placeholder="password" />
                <input type="password" className="form" id="password_repeated" placeholder="password again" />
                <button className="button"> Register </button>
            </div>
        </div>)
}
