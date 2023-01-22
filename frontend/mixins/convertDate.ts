export const convertDate = (date: string) => {
  return date.toString().slice(0, 19).replace('T', ' ')
}