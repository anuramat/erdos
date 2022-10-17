import 'registration.scss';
import 'bootstrap/dist/css/bootstrap.min.css';

export const Registration = () => {
    return (
        <div className="background">
            <div className="middle-column">
                <div className="index-message"> xd xd xd </div>
                <input type="email" class="form" id="email" placeholder="email" />
                <input type="password" class="form" id="password" placeholder="password" />
                <input type="password" class="form" id="password_repeated" placeholder="password again" />
                <button className="button"> Register </button>
            </div>
        </div>)
}
