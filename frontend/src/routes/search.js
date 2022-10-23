import 'papers.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Papers, Tabs } from 'components/papers';
import { Post } from 'components/post';
import { useSearchParams, createSearchParams } from "react-router-dom";
import { StrictMode, useEffect, useState } from 'react';
import queryString from 'query-string';
import { useForm } from 'react-hook-form';

export const Search = () => {
    const [posts, setPosts] = useState([]);
    const [searchParams, setSearchParams] = useSearchParams();
    const { register, handleSubmit } = useForm({ defaultValues: queryString.parse(window.location.search) });

    const LoadingError = () => {
        return (
            <div className="content-container mt-5">whoops</div>
        )
    }

    const searchHandler = (form) => {
        // TODO remove hardcode from url string
        setSearchParams(form)
        fetch('http://localhost:8080/search?' + queryString.stringify(form), { method: "GET" })
            .then(response => response.json()).then(papers =>
                setPosts(papers.map((paper) => Post({ paper: paper })))).catch(() => setPosts(LoadingError()));
    }

    useEffect(() => {
        searchHandler(queryString.parse(window.location.search))
    }, [])

    const result = () => {
        return (<div>
            <form onSubmit={handleSubmit((e) => searchHandler(e))}>
                <input className="form mt-5" placeholder='year' {...register("year")}></input>
                <input className="form" placeholder='author' {...register("author")}></input>
                <input type="submit" className="button" />
            </form>
            {posts}
        </div>
        )
    }
    return Papers({ tab: Tabs.search, content: result });
}

