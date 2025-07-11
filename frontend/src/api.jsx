import { useState } from "react";

async function fetchPosts () {

    const[post, setPost] = useState([])
    const[loading, setLoading] = useState(true)

    try {
        let responce = await fetch(API)

        if(!responce.ok){
            throw new Error('не получилось загрузить посты')
        }

        let result = await responce.json()
        setLoading(false)

        setPost(result)
    } catch (error) {
        console.error('Не получилось загрузить посты')
    }

    return post
}

export default fetchPosts