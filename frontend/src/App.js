import logo from './logo.svg';
import './App.scss';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
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

function sign_up_page() {
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

function log_in_page() {
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

export default App;
