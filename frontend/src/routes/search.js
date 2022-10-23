import 'papers.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Papers, Tabs } from 'components/papers';
import { Post } from 'components/post';
import { useSearchParams } from "react-router-dom";
import { useEffect, useState } from 'react';
import queryString from 'query-string';
import { useForm } from 'react-hook-form';

export const Search = () => {
    const [posts, setPosts] = useState([]);
    const [searchParams, setSearchParams] = useSearchParams();
    const { register, handleSubmit } = useForm({ defaultValues: queryString.parse(window.location.search) });

    const LoadingError = (e) => {
        let desc = ""
        switch (e) {
            case 401:
                desc = "not authenticated";
                break;
            default:
                desc = "whoops";
        }
        return (
            <div className="content-container mt-5">{desc}</div>
        )
    }

    const searchResponseHandler = (response) => {
        if (response.status === 401) {
            throw 401;
        }
        return response
    }

    const root = window.location.protocol + "//" + window.location.hostname + ":8080/";

    const searchHandler = (form) => {
        setSearchParams(form)
        fetch(root + 'search?' + queryString.stringify(form), { method: "GET" })
            .then(response => searchResponseHandler(response))
            .then(response => response.json())
            .then(papers => setPosts(papers.map(paper => Post({ paper: paper }))))
            .catch((e) => setPosts(LoadingError(e)));
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

