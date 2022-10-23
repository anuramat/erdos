import 'index.scss';

export const Post = (props) => {
    return (<div key={props.paper.id} className="content-container mt-5">
        {JSON.stringify(props.paper)}
    </div>)
}