import { message, fail, danger } from 'danger'

// Critical:
console.log(JSON.stringify(danger.git))
console.log(danger.github.pr.user.login)

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
