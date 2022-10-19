import 'papers.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Papers, Tabs } from 'components/papers';
import { Post } from 'components/post';
import { useSearchParams } from "react-router-dom";
import { useEffect, useState } from 'react';

export const Search = () => {
    const [posts, setPosts] = useState([]);
    const [searchParams, setSearchParams] = useSearchParams();
    useEffect(() => {
        fetch('http://localhost:8080/papers', { method: "GET" })
            .then(response => response.json()).then(papers =>
                setPosts(papers.map((paper) => Post({ paper: paper }))));
    })
    return Papers({ tab: Tabs.search, query: searchParams.get("q"), content: posts });
}

