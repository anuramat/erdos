import 'papers.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Papers, Tabs } from 'components/papers';
import { Post } from 'components/post';
import { useEffect, useState } from 'react';
import queryString from 'query-string';
import { getJWT } from 'auth';


// TODO for now uses stuff for posts, will have to be disentangled later
export const Authors = () => {

    const [authors, setAuthors] = useState([]);


    const LoadingError = () => {
        return (
            < div className="content-container mt-5" > whoops</div >
        );
    };

    // TODO proper error handling
    const searchHandler = (form) => {

        var myHeaders = new Headers();
        myHeaders.append("Authorization", "Bearer " + getJWT());
        // TODO fix address
        const backend_address = window.location.protocol + "//" + window.location.hostname + ":8080/";
        fetch(backend_address + 'authors/best/1', { method: "GET", headers: myHeaders })
            .then(response => response.json())
            .then(papers => setAuthors(papers.map(paper => Post({ paper: paper }))))
            .catch((e) => setAuthors(LoadingError(e)));
    };

    useEffect(() => {
        searchHandler(queryString.parse(window.location.search));
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return (
        <Papers tab={Tabs.authors}>
            {authors}
        </Papers>
    );
}

