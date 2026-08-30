import { getOfflineChatReply } from '../../app/utils/offlineChat'

interface ChatBody {
  messages?: Array<{ role: string; text?: string; content?: string }>
  locale?: string
}

export default defineEventHandler(async (event) => {
  const body = await readBody<ChatBody>(event).catch(() => ({} as ChatBody))
  const locale = body?.locale === 'en' ? 'en' : 'es'
  const lastMessage = body?.messages?.length
    ? body.messages[body.messages.length - 1]?.text || body.messages[body.messages.length - 1]?.content || ''
    : ''

  const reply = getOfflineChatReply(lastMessage, locale)
  return { reply }
})
