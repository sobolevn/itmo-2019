import { fail, danger } from 'danger'

// Critical:
if (danger.github.base.ref !== 'master') {
  fail('We only accept PRs to `master` branch.')
}

if (danger.github.head.ref.match(/homework-\d+/)) {
  fail('Your branch should be named `homework-${HOMEWORK_NUMBER}`.')
}
