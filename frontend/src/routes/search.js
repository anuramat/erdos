import 'papers.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Papers, Tabs } from 'components/papers';
import { Post } from 'components/post';
import { useSearchParams } from "react-router-dom";
import { useEffect, useState } from 'react';
import queryString from 'query-string';
import { useForm } from 'react-hook-form';
import { getJWT } from 'auth';

export const Search = () => {

    const [posts, setPosts] = useState([]);
    const [, setSearchParams] = useSearchParams();
    const { register, handleSubmit } = useForm({ defaultValues: queryString.parse(window.location.search) });

    const LoadingError = () => {
        return (
            < div className="content-container mt-5" > whoops</div >
        )
    }
    // TODO proper error handling
    const searchHandler = (form) => {

        var myHeaders = new Headers();
        myHeaders.append("Authorization", "Bearer " + getJWT());
        // TODO fix address
        const backend_address = window.location.protocol + "//" + window.location.hostname + ":8080/";
        setSearchParams(form)
        fetch(backend_address + 'search?' + queryString.stringify(form), { method: "GET", headers: myHeaders })
            .then(response => response.json())
            .then(papers => setPosts(papers.map(paper => Post({ paper: paper }))))
            .catch((e) => setPosts(LoadingError(e)));
    }

    useEffect(() => {
        searchHandler(queryString.parse(window.location.search))
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])

    return (
        <Papers tab={Tabs.search}>
            <form onSubmit={handleSubmit(searchHandler)}>
                <input className="form" placeholder='year' {...register("year")} />
                <input className="form" placeholder='author' {...register("author")} />
                <input className="form" placeholder='tag' {...register("tag")} />
                <input type="submit" className="button" />
            </form>
            {posts}
        </Papers>
    )
}

