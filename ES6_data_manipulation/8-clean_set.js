export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }

  const filtered = [...set].filter(value => value.startsWith(startString));
  const trimmed = filtered.map(value => value.slice(startString.length));
  return trimmed.join('-');
}
