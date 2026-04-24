import { useEffect, useState } from 'react'

const MOCK_RECORDS = [
  { id: 'CAPA-2041', type: 'CAPA', title: 'OOS investigation — Lot MTX-204 fill weight variance', source: 'MasterControl', owner: 'J. Okafor', status: 'Open', due: '2025-02-14', overdue: true },
  { id: 'CC-0318', type: 'Change Control', title: 'Transfer MTX-001 drug substance process to CDMO (Lonza)', source: 'MasterControl', owner: 'S. Patel', status: 'In Review', due: '2025-03-02', overdue: false },
  { id: 'BR-MTX204', type: 'Batch Record', title: 'MTX-001 DP Lot MTX-204 — executed batch record', source: 'Veeva Vault', owner: 'QA Ops', status: 'Pending Review', due: '2025-02-10', overdue: true },
  { id: 'CAPA-2039', type: 'CAPA', title: 'Environmental monitoring excursion — Cleanroom B', source: 'MasterControl', owner: 'R. Chen', status: 'Open', due: '2025-02-28', overdue: false },
  { id: 'DEV-0891', type: 'Deviation', title: 'HPLC column equilibration outside SOP window', source: 'LabWare LIMS', owner: 'M. Alvarez', status: 'Open', due: '2025-02-07', overdue: true },
  { id: 'SOP-QC-112', type: 'Controlled Doc', title: 'SOP-QC-112 Rev 4 — Release testing for DP lots', source: 'Veeva Vault', owner: 'QA Docs', status: 'Effective', due: '—', overdue: false },
  { id: 'CC-0321', type: 'Change Control', title: 'Add stability indicating assay to BLA-enabling panel', source: 'MasterControl', owner: 'L. Nguyen', status: 'Draft', due: '2025-04-01', overdue: false },
  { id: 'CAPA-2044', type: 'CAPA', title: 'Supplier qualification gap — single-use assemblies', source: 'Manual (SharePoint)', owner: 'T. Brooks', status: 'Open', due: '2025-02-20', overdue: false },
  { id: 'BR-MTX205', type: 'Batch Record', title: 'MTX-001 DS Lot MTX-205 — engineering run', source: 'Veeva Vault', owner: 'Mfg Sci', status: 'Open', due: '2025-03-15', overdue: false },
  { id: 'COA-MTX204', type: 'Lot Data', title: 'Certificate of Analysis — DP Lot MTX-204', source: 'LabWare LIMS', owner: 'QC', status: 'Pending QA', due: '2025-02-09', overdue: true },
]

function StatCard({ label, value, accent }) {
  return (
    <div className="rounded-lg border border-slate-200 bg-white p-4">
      <div className="text-xs uppercase tracking-wide text-slate-500">{label}</div>
      <div className={`mt-1 text-2xl font-semibold ${accent || 'text-slate-900'}`}>{value}</div>
    </div>
  )
}

export default function App() {
  const [health, setHealth] = useState('checking…')
  useEffect(() => {
    fetch('/api/health').then(r => r.json()).then(d => setHealth(d.status || 'ok')).catch(() => setHealth('offline'))
  }, [])

  const openCAPAs = MOCK_RECORDS.filter(r => r.type === 'CAPA' && r.status === 'Open').length
  const changeControls = MOCK_RECORDS.filter(r => r.type === 'Change Control').length
  const batchRecords = MOCK_RECORDS.filter(r => r.type === 'Batch Record').length
  const overdue = MOCK_RECORDS.filter(r => r.overdue).length

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">
      <header className="border-b border-slate-200 bg-white">
        <div className="mx-auto max-w-7xl px-6 py-4 flex items-center justify-between">
          <div>
            <div className="text-sm text-slate-500">Meridian Therapeutics, Inc.</div>
            <h1 className="text-lg font-semibold">Quality Operations — Unified View</h1>
          </div>
          <div className="text-xs text-slate-500">API: <span className="font-mono">{health}</span></div>
        </div>
      </header>

      <main className="mx-auto max-w-7xl px-6 py-8 space-y-6">
        <section>
          <h2 className="text-xl font-semibold tracking-tight">One quality system built for BLA-stage GMP</h2>
          <p className="text-sm text-slate-600 mt-1 max-w-3xl">Connect your controlled documents, CAPA workflows, and LIMS data in a single audit-ready environment as you scale toward BLA-enabling activities.</p>
        </section>

        <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <StatCard label="Open CAPAs" value={openCAPAs} />
          <StatCard label="Change Controls" value={changeControls} />
          <StatCard label="Batch Records" value={batchRecords} />
          <StatCard label="Overdue Items" value={overdue} accent="text-rose-600" />
        </section>

        <section className="rounded-lg border border-slate-200 bg-white overflow-hidden">
          <div className="px-4 py-3 border-b border-slate-200 flex items-center justify-between">
            <h3 className="font-semibold">Unified Quality Records</h3>
            <span className="text-xs text-slate-500">Sources: MasterControl · Veeva Vault · LabWare LIMS · SharePoint</span>
          </div>
          <table className="w-full text-sm">
            <thead className="bg-slate-50 text-slate-600 text-xs uppercase tracking-wide">
              <tr>
                <th className="text-left px-4 py-2">ID</th>
                <th className="text-left px-4 py-2">Type</th>
                <th className="text-left px-4 py-2">Title</th>
                <th className="text-left px-4 py-2">Source</th>
                <th className="text-left px-4 py-2">Owner</th>
                <th className="text-left px-4 py-2">Status</th>
                <th className="text-left px-4 py-2">Due</th>
              </tr>
            </thead>
            <tbody>
              {MOCK_RECORDS.map(r => (
                <tr key={r.id} className="border-t border-slate-100 hover:bg-slate-50">
                  <td className="px-4 py-2 font-mono text-xs">{r.id}</td>
                  <td className="px-4 py-2">{r.type}</td>
                  <td className="px-4 py-2">{r.title}</td>
                  <td className="px-4 py-2 text-slate-600">{r.source}</td>
                  <td className="px-4 py-2 text-slate-600">{r.owner}</td>
                  <td className="px-4 py-2">{r.status}</td>
                  <td className={`px-4 py-2 ${r.overdue ? 'text-rose-600 font-medium' : 'text-slate-600'}`}>{r.due}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      </main>
    </div>
  )
}