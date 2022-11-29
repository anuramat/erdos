import 'papers.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Menu } from 'components/menu';


export const Tabs = {
    recent: "recent",
    recommended: "recommended",
    search: "search",
    authors: "authors"
};

// props: tab
export const Papers = (props) => {

    return (
        <div className="background p-5">
            <div className="row">

                <div className="col-3">

                    <Menu />

                </div>
                <div className="col ms-5">

                    <div className="content-container">
                        <ul className="nav nav-pills nav-justified mb-5">
                            <li className="nav-item">
                                <a className={"nav-link" + (props.tab === Tabs.recommended ? " active" : "")} aria-current="page" href="/recommended">Recommended</a>
                            </li>
                            <li className="nav-item">
                                <a className={"nav-link" + (props.tab === Tabs.recent ? " active" : "")} aria-current="page" href="/recent">Recent</a>
                            </li>
                            <li className="nav-item">
                                <a className={"nav-link" + (props.tab === Tabs.search ? " active" : "")} aria-current="page" href="/search">Search</a>
                            </li>
                            <li className="nav-item">
                                <a className={"nav-link" + (props.tab === Tabs.authors ? " active" : "")} aria-current="page" href="/authors">Authors</a>
                            </li>
                        </ul>

                        {props.children}

                    </div>
                </div>
            </div>

        </div >
    );
}

