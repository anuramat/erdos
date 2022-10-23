import 'papers.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Papers, Tabs } from 'components/papers';

export const Recent = () => {

    return Papers({
        tab: Tabs.recent,
        content: () => (<div className='content-container mt-5'>nothing here yet</div>)
    })

}

