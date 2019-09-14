import { danger, fail, warn } from 'danger'

// Critical:
if (danger.github.pr.base.ref !== 'master') {
  fail('We only accept PRs to `master` branch.')
}

if (!danger.github.pr.head.ref.match(/homework-\d+/)) {
  fail('Your branch should be named `homework-${HOMEWORK_NUMBER}`.')
}

if (!danger.github.pr.mergeable) {
  fail('Looks like your PR cannot be merged, please fix it: reopen or rebase.')
}

// Warnings:
const importantFiles = [
  '.github/workflows/build.yml',
  '.github/workflows/review.yml',
  '.github/CODEOWNERS',
  '.github/pull_request_template',

  'dangerfile.ts',
  'Makefile',
  'pyproject.toml',
  'setup.cfg',
  '.gitignore',
  '.editorconfig',

  'LICENSE',
  'README.md',
  'CONTRIBUTING.md',
  'CODE_OF_CONDUCT.md',
]

const changedFiles = [
  ...danger.git.modified_files,
  ...danger.git.created_files,
  ...danger.git.deleted_files,
]

for (const changedFile of changedFiles) {
  if (!changedFile.startsWith(`students/${danger.github.pr.user.login}`)) {
    warn(`File change outside the workdir: ${changedFile}`)
  }

  if (importantFiles.includes(changedFile)) {
    warn(`Changed an important file: ${changedFile}`)
  }
}
