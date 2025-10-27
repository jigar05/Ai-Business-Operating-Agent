import { useState } from 'react'


export default function App(){
const [messages, setMessages] = useState([])
const [text, setText] = useState("")


async function send(){
if(!text) return
setMessages(prev => [...prev, {from:'user', text}])
const res = await fetch('/api/chat', {
method: 'POST',
headers: {'Content-Type': 'application/json'},
body: JSON.stringify({user_id: 'u1', prompt: text})
})
const data = await res.json()
setMessages(prev => [...prev, {from:'bot', text: data.reply}])
setText("")
}


return (
<div className="container">
<h1>AI Business Agent (MVP)</h1>
<div className="chatbox">
{messages.map((m,i)=>(
<div key={i} className={m.from==='user'? 'msg user' : 'msg bot'}>{m.text}</div>
))}
</div>
<div className="composer">
<input value={text} onChange={e=>setText(e.target.value)} placeholder="Type a prompt..."/>
<button onClick={send}>Send</button>
</div>
</div>
)
}
