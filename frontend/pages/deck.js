import { useEffect, useState } from 'react'

const API = process.env.NEXT_PUBLIC_API_BASE

export default function Deck(){
  const [pw,setPw] = useState('')
  const [msg,setMsg] = useState('')
  const [ok,setOk] = useState(false)
  const [email,setEmail] = useState('')

  useEffect(()=>{
    const u = new URL(window.location.href)
    const e = u.searchParams.get('e') || ''
    setEmail(e)
    if(API){
      fetch(`${API}/analytics/track`, {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({ type:'deck_view', id:'web', email:e, ts: Date.now() })
      }).catch(()=>{})
    }
  },[])

  async function unlock(e){
    e.preventDefault()
    setMsg('Unlocking…')
    try{
      const r = await fetch(`${API}/deck/unlock`, {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({ password: pw })
      })
      if(!r.ok){ const t = await r.text(); throw new Error(t || r.statusText) }
      setOk(true); setMsg('Unlocked.')
      fetch(`${API}/analytics/track`, {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({ type:'deck_open', id:'web', email, ts: Date.now() })
      }).catch(()=>{})
    }catch(err){
      setOk(false); setMsg('Invalid password')
    }
  }

  function onCalendlyClick(){
    if(API){
      fetch(`${API}/analytics/track`, {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({ type:'link_click', where:'calendly', id:'web', email, ts: Date.now() })
      }).catch(()=>{})
    }
  }

  return (
    <div>
      <header>
        <div className="logo">C</div>
        <b>Investor Deck</b>
      </header>
      <div className="container">
        {!ok ? (
          <form onSubmit={unlock} className="card" style={{maxWidth:480}}>
            <h2>Enter Access Code</h2>
            <input className="input" value={pw} onChange={e=>setPw(e.target.value)} placeholder="Password" type="password"/>
            <div style={{height:12}}/>
            <button className="btn" type="submit">Unlock</button>
            <div style={{height:8}}/>
            <small>{msg}</small>
          </form>
        ) : (
          <div className="card">
            <h2>Deck Unlocked</h2>
            <p>Replace this block with your embedded slides or a link to your PDF.</p>
            <p><a className="btn" href="https://calendly.com/" onClick={onCalendlyClick}>Book a 15‑min call</a></p>
          </div>
        )}
      </div>
      <footer className="container"><small>© CapitalConductor</small></footer>
    </div>
  )
}
