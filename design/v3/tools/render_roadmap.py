#!/usr/bin/env python3
"""Render readable task detail from the authoritative roadmap registry."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    roadmap = json.loads((ROOT/'manifests/development-roadmap.json').read_text())
    text = '# V3 task-by-task implementation list\n\nFuture development tasks; proposed filenames are targets, not files already created. The [tracker](../manifests/development-roadmap.json) owns task state and dependencies.\n'
    for phase in roadmap['phases']:
        text += f'\n## {phase["id"]} — {phase["title"]}\n\nExit: {phase["exit"]}\n'
        for task in (t for t in roadmap['tasks'] if t['phase'] == phase['id']):
            text += f'\n### {task["id"]} — {task["title"]}\n\n'
            fields = [('Status', task['status']),
                      ('Depends on', ', '.join(task['depends_on']) or 'None'),
                      ('Pages', ', '.join(task['page_ids']) or 'Shared/global work'),
                      ('Deliverable', ' '.join(task['deliverables'])),
                      ('Acceptance', ' '.join(task['acceptance'])),
                      ('Proposed targets', '; '.join(task['file_targets']))]
            if task['inputs']:
                fields.append(('Inputs', '; '.join(task['inputs'])))
            for label, value in fields:
                text += f'- **{label}:** {value}\n'
    (ROOT/'development/tasks.md').write_text(text.rstrip()+'\n')
    print(f'Rendered {len(roadmap["tasks"])} tasks.')


if __name__ == '__main__':
    main()
