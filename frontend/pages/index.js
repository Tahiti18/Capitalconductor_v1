export default function Home(){
  return (
    <div>
      <header>
        <div className="logo">C</div>
        <b>CapitalConductor</b>
      </header>
      <div className="container">
        <h1>Funding, orchestrated.</h1>
        <p>Minimal Next.js frontend wired to your backend. Use the Deck page to unlock and the Press/Launch pages for quick content stubs.</p>
        <div className="grid">
          <a className="card" href="/deck"><h3>Investor Deck →</h3><small>Password gate + analytics</small></a>
          <a className="card" href="/launch"><h3>Launch →</h3><small>CTA section</small></a>
          <a className="card" href="/press"><h3>Press →</h3><small>Press-ready text stub</small></a>
        </div>
      </div>
      <footer className="container"><small>© CapitalConductor</small></footer>
    </div>
  )
}
