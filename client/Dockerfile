FROM node:20.9.0-alpine AS base


# install dependensies
FROM base AS deps

RUN apk add --no-cache libc6-compat

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci


# live dev
FROM base AS dev

WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules
COPY . .


# build the project
FROM base AS builder

WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules
COPY . .

RUN yarn build


# run production
FROM base AS runner

WORKDIR /app

RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/ ./.next/

USER nextjs

CMD ["yarn", "start"]
